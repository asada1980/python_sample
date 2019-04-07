import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)

print(type(x))

x1 = np.array([1.0, 2.0, 3.0])
y1 = np.array([0.5, 1.0, 1.0])
#足し算
print(x1 + y1)

#引き算
print(x1 - y1)

#掛け算
print(x1 * y1)

#割り算
print(x1 / y1)

#ブロードキャスト
print(x1 * 2)


#要素へのアクセス
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)

print(X[0])

print(X[0][1])

#2次元配列を1次元配列へ
print(X.flatten())
X = X.flatten()
print(X[np.array([0, 2, 4])])

#抽出（boolean）
print( X > 15)

#抽出（値）
print( X[X>15])

