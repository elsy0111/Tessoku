import io
import sys

_INPUT = """\
5 3
6 11 2 5 5
5
20
0

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
import bisect
import itertools
N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
As = list(itertools.accumulate(A))
sum_N = As[-1]
print(A)
print(As)
print(sum_N)
for _ in range(Q):
    X = int(input())
    k = bisect.bisect_right(A,X)
    print(X,k)
    sum_ak = As[k-1]
    print(sum_ak)
    print(sum_N - sum_ak)
    ans = k * X - sum_ak + sum_N - sum_ak - (N - k) * X
    print(ans)
