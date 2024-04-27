---
title: 
draft: false
tags: 
date: 2024-04-27
---
## 生成一个数字矩阵

```python
# 生成一个 5x5 的数字矩阵
matrix = [[i + 1 for i in range(5 * j, 5 * (j + 1))] for j in range(5)]

# 打印矩阵
for row in matrix:
    print(row)

```

