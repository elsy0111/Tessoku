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
from itertools import product
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

# 配列A,B,C,Dの各要素の最大値と最小値を求める
max_value = max(max(A), max(B), max(C), max(D))
min_value = min(min(A), min(B), min(C), min(D))

# 配列A,B,C,Dから同時に要素を選ぶ
combinations = product(A, B, C, D)

# 各組み合わせで、最大値と最小値の差を計算する
min_difference = float('inf')
for combination in combinations:
    max_value = max(combination)
    min_value = min(combination)
    difference = max_value - min_value
    if difference < min_difference:
        min_difference = difference

# 結果を出力する
print(min_difference)  # 最小値