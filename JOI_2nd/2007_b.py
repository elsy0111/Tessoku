import io
import sys

_INPUT = """\
3
1
4
5
7
9
6
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
deq = [0 for _ in range(30)]
for _ in range(28):
    i = int(input())
    deq[i - 1] = 1
for i in range(30):
    if deq[i] == 0:
        print(i + 1)