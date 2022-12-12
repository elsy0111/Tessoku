import io
import sys

_INPUT = """\
1 6
1 2 2 3 2 1
"""

sys.stdin = io.StringIO(_INPUT)

#------------------------------
import itertools
H,W = map(int,input().split())

Arr = list(map(int,input().split()))
A = set()
for ai in Arr:
    A.add(ai)
A = list(A)
print(A)
max_score = 0
fill = [0 for _ in range(len(A))]
L = [(k, list(g)) for k, g in itertools.groupby(Arr)]
for i in L:
    print(i)
    print(len(i[1]))
# 各マスを走査
for Ai in A:
    A_score = 0
    score = 0
    for x in range(W):
        if Ai == Arr[x]:
            A_score += 1
    if max_score < A_score:
        max_score = A_score

print(max_score)