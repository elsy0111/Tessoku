import io
import sys

_INPUT = """\
5 5 2
1 1 3 3
2 2 4 4

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
# n = int(input())
# h = list(map(int,input().split()))
H,W,N = map(int,input().split())
ar = [[0] * (W + 2) for _ in range(H + 2)]
def sum_2d(arr):
    n = len(arr)
    m = len(arr[0])
    cum_sum = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            cum_sum[i][j] = cum_sum[i-1][j] + cum_sum[i][j-1] - cum_sum[i-1][j-1] + arr[i-1][j-1]
    
    return cum_sum
for _ in range(N):
    A,B,C,D = map(int,input().split())
    ar[A][B] += 1
    ar[C + 1][D + 1] += 1
    ar[A][D + 1] -= 1
    ar[C + 1][B] -= 1
ar = sum_2d(ar)
for i in range(1,H + 1):
    for j in range(1,W + 1):
        print(ar[i + 1][j + 1],end = " ")
    print()