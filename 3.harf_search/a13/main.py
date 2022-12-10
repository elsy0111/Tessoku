import io
import sys

_INPUT = """\
7 10
11 12 16 22 27 28 31

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
N, K = map(int, input().split())
A = list(map(int, input().split()))
deq = []
ans = 0
for x in A:
    deq.append(x)
    while (deq[-1] - deq[0]) > K:
        del deq[0]
    ans += len(deq) - 1
print(ans)