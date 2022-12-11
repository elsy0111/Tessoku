import io
import sys

_INPUT = """\
4 2 2
1 2 3 4

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
K,N,D = map(int,input().split())
A = list(map(int,input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# D の約数を求める
divisors = [make_divisors(D)]

# D の約数が最大となる値を求める
max_divisor_sum = 0
for i in range(N-K+1):
    divisor_sum = 0
    for j in range(K):
        divisor_sum += A[i+j]
    if divisor_sum > max_divisor_sum:
        max_divisor_sum = divisor_sum

# D の倍数かどうかを判定する
if max_divisor_sum % D == 0:
    print(max_divisor_sum)
else:
    print(-1)