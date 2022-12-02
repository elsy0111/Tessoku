import io
import sys

_INPUT = """\


"""

# sys.stdin = io.StringIO(_INPUT)

#----------------------------------
D = int(input())
N = int(input())
A = [0 for _ in range(D + 2)]
for _ in range(N):
    L,R = map(int,input().split())
    A[L] += 1
    A[R + 1] -= 1
for i in range(1,D + 1):
    A[i] += A[i - 1]
for i in range(D):
    print(A[i + 1])