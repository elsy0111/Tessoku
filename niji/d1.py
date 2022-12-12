import io
import sys

_INPUT = """\
5 2 12
40 30 20 10

"""

sys.stdin = io.StringIO(_INPUT)

#----------------------------------
# n = int(input())
N,W,D = map(int,input().split())
A = list(map(int,input().split()))

# 各駅から駅 1 までの距離
distances = [0] * N
for i in range(2, N):
    distances[i] = distances[i - 1] + 1

# 貨物列車の現在地
current = 1
# 貨物列車が積んでいる貨物の価値の合計
total = 0
# 貨物列車が積んでいる貨物の数
count = 0

# 貨物列車が駅 1 に到達するまで移動する
while current != 1:
    # 貨物列車が移動できる距離を超えている場合、駅 1 に到達するまで走行する
    if distances[current] > D:
        current = 1
        continue

    # 貨物列車が積める貨物を決める
    for i in range(current - 1, 1, -1):
        # 貨物列車がその駅に到達するまでに走った距離が D 以下で、
        # かつ、貨物列車に積まれている貨物の数が W 以下の場合、
        # 貨物列車に貨物を積む
        if distances[i] <= D and count < W:
            total += A[i]
            count += 1
    # 貨物列車を移動する
    current -= 1

# 最終的に駅 1 に置かれている貨物の価値の合計を出力する
print(total)