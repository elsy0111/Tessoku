import io
import sys

_INPUT = """\
15 47
11 13 17 19 23 29 31 37 41 43 47 53 59 61 67
"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
# n = int(input())
# h = list(map(int,input().split()))
N,X = map(int,input().split())
A = [0] + list(map(int,input().split()))
L = 1
R = N
while L <= R:
    M = int((L + R) / 2)
    if X < A[M]:
        R = M - 1
    elif X > A[M]:
        L = M + 1
    else:
        print(M)
        break
