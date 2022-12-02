import io
import sys

_INPUT = """\


"""

# sys.stdin = io.StringIO(_INPUT)

#----------------------------------

H,W = map(int,input().split())
X = [[]for _ in range(H + 1)]
X[0] = [0 for _ in range(W + 1)]
for i in range(1,H + 1):
    X[i] += [0] + list(map(int,input().split()))
Q = int(input())
for i in range(1,H + 1):
    for j in range(1,W + 1):
        X[i][j] += X[i][j - 1]
for i in range(1,W + 1):
    for j in range(1,H + 1):
        X[j][i] += X[j - 1][i]
for _ in range(Q):
    A,B,C,D = map(int,input().split())
    S = X[C][D] + X[A - 1][B - 1] - X[A - 1][D] - X[C][B - 1]
    print(S)