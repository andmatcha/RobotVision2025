import numpy as np

# 任意の2*3の行列
array1 = np.array([[1, 2, 3], [4, 5, 6]])

# array1の形状を表示
print("array1 shape: ", array1.shape)

# numpy.random.randを用いて配列長100の乱数を生成し，変数array2に格納
array2 = np.random.rand(100)

# スライスを用いて11〜20番目(1-indexed)の要素を表示
print("array2[10:20]:\n", array2[10:20])

# numpy.sortとスライスを用いて，array2を降順にソート
array2 = np.sort(array2)[::-1]

# array2中の各要素の2乗を計算し表示
array2_squared = array2 ** 2
print("array2 squared:\n", array2_squared)
