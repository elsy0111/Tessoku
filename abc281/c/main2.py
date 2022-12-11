import io
import sys

_INPUT = """\
3 600
180 240 120

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
N, T = map(int, input().split())
A = list(map(int, input().split()))

L = sum(A)

t = T % L
for i in range(N):
    a = A[i]
    t -= a
    if t < 0:
        print(i + 1,end = " ")
        print(a + t)
        exit()