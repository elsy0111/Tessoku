import io
import sys

_INPUT = """\
3 600
180 240 120

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
N,T = map(int,input().split())
A = list(map(int,input().split()))

cum_sum = [0]
i = 0
while T > cum_sum[-1]:
    if i == N:
        i = 0
    i += 1
    cum_sum.append(cum_sum[-1] + A[i-1])
print(i,T - cum_sum[-2])