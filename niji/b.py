import io
import sys

_INPUT = """\
7
7 9 9 4 6 3 5
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

max_A = max(A)
min_A = min(A)
max_B = max(B)
min_B = min(B)
max_C = max(C)
min_C = min(C)
max_D = max(D)
min_D = min(D)

# 全部で8通りの組み合わせを計算する
min_difference = float('inf')
for a in [max_A, min_A]:
    for b in [max_B, min_B]:
        for c in [max_C, min_C]:
            for d in [max_D, min_D]:
                max_value = max(a, b, c, d)
                min_value = min(a, b, c, d)
                difference = max_value - min_value
                if difference < min_difference:
                    min_difference = difference

# 結果を出力する
print(min_difference)  # 最小値