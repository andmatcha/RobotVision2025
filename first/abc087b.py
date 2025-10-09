# あなたは、500 円玉をA 枚、100 円玉をB 枚、50 円玉をC 枚持っています。 これらの硬貨の中から何枚かを選び、合計金額をちょうどX 円にする方法は何通りありますか。同じ種類の硬貨どうしは区別できません。2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。

# 制約
# 0 ≤ A, B, C ≤ 50
# A + B + C ≥ 1
# 50 ≤ X ≤ 20000
# A, B, C は整数である
# X は50 の倍数である

# 入力は標準入力で以下の形式
# A
# B
# C
# X

A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            if 500 * a + 100 * b + 50 * c == X:
                count += 1

print(count)
