import io
import sys

_INPUT = """\
3

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
# n = int(input())
# h = list(map(int,input().split()))
# a,b = map(int,input().split())

N = int(input())
for i in range(N,-1,-1):
    print(i)