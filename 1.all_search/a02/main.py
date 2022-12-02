import io
import sys

_INPUT = """\


"""

# sys.stdin = io.StringIO(_INPUT)

#----------------------------------
n,x = map(int,input().split())
a = list(map(int,input().split()))
b = False
for ai in a:
    if x == ai:
       b = True
if b == True:
    print("Yes")
else:
    print("No")
