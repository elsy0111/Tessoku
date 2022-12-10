import io
import sys

_INPUT = """\
4 10
1 2 3 4

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
# n = int(input())
# h = list(map(int,input().split()))
# a,b = map(int,input().split())

N,K = map(int,input().split())
A = list(map(int,input().split()))
L = 1
R = 10**9

def f(Mid):
    sum = 0
    for i in range(N):
        sum += int(Mid / A[i])
    return sum

while L < R:
    M = int((L + R)/2)
    s = f(M)
    if s >= K:
        R = M
    else:
        L = M + 1
print(L)
