import io
import sys

_INPUT = """\
5
"""

# sys.stdin = io.StringIO(_INPUT)

#----------------------------------
n = int(input())
a = [0 for _ in range(10)]
for i in range(10):
    if int(n / (1 << i)) % 2 == 1:
        a[i] = 1
    else:
        a[i] = 0
a.reverse()
print(*a,sep="")
