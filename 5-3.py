import numpy as npy

x0 = npy.ones(10)
x1 = npy.array([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
x2 = npy.array([2, 3, 4, 2, 3, 4, 2, 4, 1, 3])
y = npy.array([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

X = npy.stack((x0, x1, x2), axis=1)

Y = npy.reshape(y, (10, 1))

X1 = npy.mat(X)
W = (X1.T * X1).I * X1.T * Y
print("w的shape属性：\n", W.shape)
print("\nX的值：\n", X)
print("\nY的值：\n", Y)
print("\nW的值：\n", W)
