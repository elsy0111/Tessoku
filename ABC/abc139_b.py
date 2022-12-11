import io
import sys

_INPUT = """\
8 9
"""

sys.stdin = io.StringIO(_INPUT)

#================================
from math import ceil
a,b = map(int,input().split())
print(ceil((b - 1)/(a - 1)))