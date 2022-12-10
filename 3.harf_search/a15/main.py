import io
import sys

_INPUT = """\
5
46 80 11 77 46

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
N = int(input())
A = list(map(int,input().split()))

# 小さい順にソートする
B = sorted(set(A))

# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v : i + 1 for i, v in enumerate(B) }

# 答え
print(*list(map(lambda v: D[v], A)))

