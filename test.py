# 外层循环控制行数（被乘数）
for i in range(1, 10):
    # 内层循环控制每行的列数（乘数）
    for j in range(1, i + 1):
        # 计算乘积
        product = i * j
        # 格式化输出，保证对齐
        print(f"{i}×{i}={product:2d}", end="\t")
    # 每行结束后换行
    print(123)

    print(121)

