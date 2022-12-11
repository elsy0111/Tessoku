import io
import sys

_INPUT = """\
10 6 3
12 2 17 11 19 8 4 3 6 20

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
N,M,K = map(int,input().split())
A = [0] + list(map(int,input().split()))

B = sorted(A[1:M+1])
for i in range(1, N - M + 2):
    print(sum(B[:K]),end = " ")
    if i + M <= N:
        B.remove(A[i])
        B.append(A[i+M])
        B = sorted(B)
print()
# N,M,K = map(int,input().split())
# A = [0] + list(map(int,input().split()))

# for i in range(1, N - M + 2):
#     B = []
#     for j in range(M):
#         B.append(A[i+j])
#     B = sorted(B)
#     print(sum(B[:K]),end = " ")
# print()