import io
import sys

_INPUT = """\

"""

# sys.stdin = io.StringIO(_INPUT)

#----------------------------------

n,k = map(int,input().split())
cnt = 0
for i in range(1,n + 1):
    for j in range(1,n + 1):
        z  = i + j
        if (k - z) >= 1 and k - z <= n:
            cnt += 1
print(cnt)
