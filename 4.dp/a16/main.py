import io
import sys

_INPUT = """\
15 30
6 9
9 10
2 9
9 1
2 14
1 4
4 6
1 3
4 14
1 6
9 11
2 6
3 9
5 9
4 9
11 15
1 13
4 13
8 9
9 13
5 15
3 5
8 10
2 4
9 14
1 9
2 8
6 13
7 9
9 15

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
# h = list(map(int,input().split()))
N,M = map(int,input().split())
graph = [0] + [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
for i in range(1,N + 1):
    print(str(i) + ":",end = " {")
    if len(graph[i]) != 0:
        for j in range(len(graph[i]) - 1):
            print(graph[i][j],end = ", ")
        print(graph[i][-1],"}",sep = "")
    else:
        print("}")
