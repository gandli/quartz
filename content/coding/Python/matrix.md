---
title: python 矩阵研究
draft: false
tags:
  - python
  - 矩阵
  - 编程
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

```bash
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
[11, 12, 13, 14, 15]
[16, 17, 18, 19, 20]
[21, 22, 23, 24, 25]
```
## 写成函数

```python
def generate_matrix(n):
    # 使用列表解析生成一个 n x n 的数字矩阵
    result = [[i + 1 for i in range(n * j, n * (j + 1))] for j in range(n)]
    # 返回生成的数字矩阵
    return result


# 调用 generate_matrix 函数生成一个 5x5 的数字矩阵
matrix = generate_matrix(5)

# 打印生成的矩阵
for row in matrix:
    print(row)
```

```bash
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
[11, 12, 13, 14, 15]
[16, 17, 18, 19, 20]
[21, 22, 23, 24, 25]
```

除了以上的`列表解析`的方法生成矩阵，还有`嵌套循环`和`第三方库`

## 嵌套循环

```python
matrix = []
num = 1
for i in range(5):
    row = []
    for j in range(5):
        row.append(num)
        num += 1
    matrix.append(row)
```

```python
def generate_matrix(n):
    result = []
    num = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(num)
            num += 1
        result.append(row)
    return result
```

# 第三方库

### `arange` 和 `reshape`

```python
# numpy 库
import numpy as np


def generate_matrix(n):
    return np.arange(1, n * n + 1).reshape(n, n)
```