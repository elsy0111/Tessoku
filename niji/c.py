import io
import sys

_INPUT = """\
4 4
1 2 3 1
2 2 3 1
1 2 3 1
3 3 2 2

"""

sys.stdin = io.StringIO(_INPUT)

#------------------------------
import sys
sys.setrecursionlimit(10**7) 
H,W = map(int,input().split())

direc = [[        [1,0,1],[2,-1,0],[3,0,-1]],
         [[0,1,0],        [2,-1,0],[3,0,-1]],
         [[0,1,0],[1,0,1],         [3,0,-1]],
         [[0,1,0],[1,0,1],[2,-1,0]         ],
         [[0,1,0],[1,0,1],[2,-1,0],[3,0,-1]]]
visited = [[False for _ in range(W)] for _ in range(H)]
# define dfs
def dfs(Ap,x,y,d):
    global score
    if x < 0 and x >= W and y < 0 and y >= H:
        return
    score += 1
    visited[x][y] = True
    for n in direc[d]:
        X = x + n[1]
        Y = y + n[2]
        if Arr[X][Y] == Ap:
            if visited[x - 1][y - 1] == False:
                dfs(Ap,X,Y,n[0])
    return score

Arr = []
for _ in range(H):
    Arr.append(list(map(int,input().split())))
A = set()
for row in Arr:
    for value in row:
        A.add(value)
A = list(A)
# JOIくんの得点として達成可能な最大値
max_score = 0

# 各マスを走査
for Ai in A:
    A_score = 0
    score = 0
    for x in range(1, H + 1):
        for y in range(1, W + 1):
            if Ai == Arr[x - 1][y - 1]:
                A_score += 1
            elif visited[x - 1][y - 1] == False:
                score += dfs(Arr[x - 1][y - 1],x-1,y-1,-1)
            # JOIくんの得点として達成可能な最大値の更新
            max_score = max(max_score, score)

# JOIくんの得点として達成可能な最大値を出力
print(max_score)