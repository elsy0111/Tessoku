import io
import sys

_INPUT = """\
10
OOOOOOOOOO

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
N = int(input())
S = [0] + list(input())
cnt = 0
i = 1
while i + 1 <= N:
    if S[i] + S[i + 1] == "OX" or S[i] + S[i + 1] == "XO":
        cnt += 1
        i += 2
    else:
        i += 1
print(cnt)
