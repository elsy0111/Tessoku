import io
import sys

_INPUT = """\
5 5
1 2 3 1 5
1 22 11 44 3
1 33 41 53 2
4 92 35 23 1
4 2 6 3 5

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
# n = int(input())
# h = list(map(int,input().split()))
H,W = map(int,input().split())
A = [[0 for _ in range(W)]]
for _ in range(H):
    A.append([0] + list(map(int,input().split())))

# min(A(i,j) * min(abs(j - n),abs(i - m)))
min_value = float("inf")
for m in range(1,H + 1):
    for n in range(1,W + 1):
        value = 0
        for i in range(1, H + 1):
            for j in range(1, W+1):
                value += A[i][j] * min(abs(j - n), abs(i - m))
        if value < min_value:
            min_value = value

print(min_value)