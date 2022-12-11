import io
import sys

_INPUT = """\
3
12 18 11

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
n = int(input())
A = list(map(int,input().split()))

# A の要素を 2 進数表記に変換する
binary_A = []
for a in A:
    binary = []
    while a > 0:
        binary.append(a % 2)
        a //= 2
    binary_A.append(binary)

# 最も高い桁から順に比較する
x = 0
for i in range(max(len(b) for b in binary_A)):
    # A の要素を 2 進数表記に変換したものの i 番目の桁について、1 と 0 の出現回数を数える
    one_count = 0
    zero_count = 0
    for b in binary_A:
        if len(b) > i:
            if b[i] == 1:
                one_count += 1
            else:
                zero_count += 1
    # 1 と 0 の出現回数が異なる場合、1 を x に選ぶことで A の最大値を最小化する
    if one_count != zero_count:
        x = 1
        break

# 最大値を最小化する x を出力する
print(x)