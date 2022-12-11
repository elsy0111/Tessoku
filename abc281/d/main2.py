# N個の整数
N = 4
# K個の整数
K = 4
# 非負整数列A
a = [1, 2, 3, 4]
# 最大値
ans = 0

# 再帰関数
def dfs(i, sum):
    global ans
    # k個の整数を選び終わった
    if i == K:
        # 答えを更新
        ans = max(ans, sum)
        return
    # N個の整数を全て試す
    for j in range(N):
        dfs(i + 1, sum + a[j])

# 最初の整数を選ぶ
dfs(0, 0)

# 答えを出力
print(ans)