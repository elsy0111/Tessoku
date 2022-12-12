import io
import sys

_INPUT = """\
10
440894064 101089692 556439322 34369336 98417847 216265879 623843484 554560874 247445405 718003331

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
N = int(input())
A = list(map(int,input().split()))

B = sorted(A)

for i in range(N):
    ans = max(A[i] - B[0],B[-1] - A[i])
    # 結果を出力する
    print(ans)