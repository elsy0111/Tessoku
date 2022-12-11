import io
import sys

_INPUT = """\
3
RRR
GGG
BBB
RGB
RGB
RGB

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
import numpy as np
N = int(input())
S = []
T = []
min_cnt = float("inf")
for _ in range(N):
    S.append(list(input()))
for _ in range(N):
    T.append(list(input()))
for i in range(4):
    Arr = np.rot90(S,i)
    if i != 3:
        cnt = i
    else:
        cnt = 1
    for x in range(N):
        for y in range(N):
            if Arr[x][y] != T[x][y]:
                cnt += 1
    min_cnt = min(cnt,min_cnt)
print(min_cnt)