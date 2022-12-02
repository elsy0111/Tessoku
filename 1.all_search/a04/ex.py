import io
import sys

_INPUT = """\
5
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())
ans = ""
for i in range(1 << 4):
    if n & (1 << i):
        ans += "1"
    else:
        ans += "0"
print(ans[::-1])
