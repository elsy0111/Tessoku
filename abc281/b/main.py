import io
import sys

_INPUT = """\
X900000

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
# n = int(input())
# h = list(map(int,input().split()))
# a,b = map(int,input().split())


S = input()

if len(S) != 8:
    print("No")
    exit()
if not S[0].isupper():
    print("No")
    exit()

try:
    num = int(S[1:7])
    if num < 100000 or num > 999999:
        print("No")
        exit()
except ValueError:
    print("No")
    exit()

if not S[7].isupper():
    print("No")
    exit()

print("Yes")