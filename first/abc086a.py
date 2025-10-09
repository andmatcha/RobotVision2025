# 1 ≤ a, b ≤ 10000
# a, b は整数
# 入力は標準入力で以下の形式
# a b

# a と b の積が奇数なら Odd と、 偶数なら Even と出力
a, b = map(int, input().split())
if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
