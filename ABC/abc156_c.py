import io
import sys

_INPUT = """\
2
1 4
"""

sys.stdin = io.StringIO(_INPUT)

#================================
from math import ceil
N = int(input())
X = list(map(int,input().split()))
alpha = sum(X)
beta = 0
Ps = ceil(alpha / N)
Pl = int(alpha / N)
for Xi in X:
    beta += Xi ** 2
print(min(N * Ps ** 2 - 2 * Ps * alpha + beta,
          N * Pl ** 2 - 2 * Pl * alpha + beta))