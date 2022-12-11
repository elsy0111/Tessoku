import io
import sys

_INPUT = """\
3 2
1 3
2 3

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
import sys
sys.setrecursionlimit(10**6)
# N = Vertex M = Node
N,M = map(int,input().split())
# 1-indexed graph
G = [0] + [[] for _ in range(N)]
# input
for i in range(M):
    A,B = map(int,input().split())
    G[A].append(B)
    G[B].append(A)
# 1-indexed visited
visited = [True] + [False for _ in range(N)]
# define dfs
def dfs(i):
    visited[i] = True
    for nex in G[i]:
        if visited[nex] == False:
            dfs(nex)
# call dfs
dfs(1)
# check visited
for v in visited:
    if v == False:
        print("The graph is not connected.")
        exit()
print("The graph is connected.")