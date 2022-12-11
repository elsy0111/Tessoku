import io
import sys

_INPUT = """\
7 3
.#.#..#


"""

sys.stdin = io.StringIO(_INPUT)

n,a = map(int,input().split())
s = ["X"] + list(input()) + ["X"]
nc = 0
step = 0
for si in s:
    if si == "#":
        nc += 1
direc = 1
current = a + 1
if current == n + 1:
    current = n - 1
    step += 2
    direc = -1
while nc > 0:
    skip = True
    if direc == 1:
        for i in range(current,n + 1,direc):
            step += 1
            if s[i] == "#":
                s[i] = "."
                nc -= 1
                direc = -1
                current = i - 1
                skip = False
                break
        if skip:
            step += 1
            current = n
            direc = -1
            continue
    else:
        for i in range(current,0,direc):
            step += 1
            if s[i] == "#":
                s[i] = "."
                nc -= 1
                direc = 1
                current = i + 1 
                skip = False
                break
        if skip:
            step += 1
            current = 1
            direc = 1
            continue

print(step)