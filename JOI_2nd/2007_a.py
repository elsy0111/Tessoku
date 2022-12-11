import io
import sys

_INPUT = """\


"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(max(sum(A),sum(B)))