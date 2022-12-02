import io
import sys

_INPUT = """\
10 5
8 6 9 1 2 1 10 100 1000 10000
2 3
1 4
3 9
6 8
1 10

"""

# sys.stdin = io.StringIO(_INPUT)

#----------------------------------
N,Q = map(int,input().split())
A = [0] + list(map(int,input().split())) + [0]
for i in range(1,N + 1):
    A[i] += A[i - 1]
for _ in range(Q):
    L,R = map(int,input().split())
    print(A[R] - A[L - 1])
