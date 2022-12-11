import io
import sys

_INPUT = """\
5 3
ABCBA
CCBAB
AAAAA


"""

sys.stdin = io.StringIO(_INPUT)

#=========================
import itertools
N,Q = map(int,input().split())
def rev(arr,k):
    print(arr,k)
    new = list(reversed(arr[:k + 1]))  + [arr[-1]]
    print(new)
    return new
for _ in range(1):
    S = list(input())
    print(S)
    # while len(S) > 3:
    for _ in range(2):
        for i in range(1,2):
            if S[-i] == S[0]:
                S = rev(S,len(S)-i)
                print(S)