import numpy as npy

index = 1
npy.random.seed(612)  # 设置随机数种子
a = npy.random.rand(1000)  # 设置范围
print("请输入一个1-100之间的整数：")
b = int(input())
for i in range(0, len(a)):
    if i % b == 0:
        print("%d   %d   %.16f\t" % (index, i, a[i]))
        index += 1
