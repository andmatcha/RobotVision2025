# 入力は標準入力で以下の形式
# N
# A_1 A_2 ​... A_N

# 制約
# 1 ≤ N ≤ 200
# 1 ≤ A_i ​≤ 10^9

# 出力
# A_iがすべて偶数の場合、すべてのA_iを2で割る操作を繰り返し、A_iのうち1つでも奇数になるまでの操作回数を出力
N = int(input())
A = list(map(int, input().split()))

count = 0
while all(a % 2 == 0 for a in A):
    A = [a // 2 for a in A]
    count += 1
print(count)
