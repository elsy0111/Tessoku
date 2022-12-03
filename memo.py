import itertools
import bisect

print("========== itertools.accumulate ==========")
arr = [1,3,5,7,9]
sum = list(itertools.accumulate(arr))
print(sum)
# -> [1, 4, 9, 16, 25]

s = ['ab', 'bc', 'cd']
print(list(itertools.accumulate(s)))
# -> ['ab', 'abbc', 'abbccd']

print("================= sum_1d =================")
arr = [1,3,5,7,9]
def sum_1d(arr):
    n = len(arr)
    cum_sum = [0 for _ in range(n+2)]
    for i in range(1,n + 1):
        cum_sum[i] = cum_sum[i - 1] + arr[i-1]
    return cum_sum
print(sum_1d(arr))
# -> [0, 1, 4, 9, 16, 25, 0]

print("================= sum_2d =================")
def sum_2d(arr):
    n = len(arr)
    m = len(arr[0])
    cum_sum = [[0] * (m+2) for _ in range(n+2)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            cum_sum[i][j] = cum_sum[i-1][j] + cum_sum[i][j-1] - cum_sum[i-1][j-1] + arr[i-1][j-1]

    return cum_sum
ar = [[1] * 4 for _ in range(5)]
for i in sum_2d(ar):
    print(i)
# ->
# [ 0,  0,  0,  0,  0, 0]
# [ 0,  1,  2,  3,  4, 0]
# [ 0,  2,  4,  6,  8, 0]
# [ 0,  3,  6,  9, 12, 0]
# [ 0,  4,  8, 12, 16, 0]
# [ 0,  5, 10, 15, 20, 0]
# [ 0,  0,  0,  0,  0, 0]

print("================= bisect =================")
print("#left")
li = [2,5,8,13,13,15,20]
idx = bisect.bisect_left(li,13)
print(idx)
# -> 3

print("#right")
li = [2,5,8,13,13,15,20]
idx = bisect.bisect_right(li,13)
print(idx)
# -> 5

print("================= arg =================")
print("#sort")
x_list = [4, 1999, 2]
i_list = sorted(range(len(x_list)), key=x_list.__getitem__)
print(i_list)
# -> [2, 0, 1]

print("#max")
x_list = [4, 1999, 2]
i_max = max(range(len(x_list)), key=x_list.__getitem__)
print(i_max )
# -> 1

print("#min")
x_list = [4, 1999, 2]
i_min = min(range(len(x_list)), key=x_list.__getitem__)
print(i_min )
# -> 2
