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

### 列表推导的方法

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
### 写成函数

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

### 嵌套循环的方法

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

### 写成函数

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
    
matrix = generate_matrix(5)    
```

## 使用第三方库

### `np` 的 `arange` 和 `reshape`

```python
# numpy 库 arange、reshape
import numpy as np


def generate_matrix(n):
    return np.arange(1, n * n + 1).reshape(n, n)
    
matrix = generate_matrix(5) 
```

输出：

```bash
[1 2 3 4 5]
[ 6  7  8  9 10]
[11 12 13 14 15]
[16 17 18 19 20]
[21 22 23 24 25]
```
### `np` 的 `random.randint`

```python
# numpy 库 random.randint
import numpy as np


def generate_matrix(n):
	return np.random.randint(1,n*n,size=(n,n))
	    
matrix = generate_matrix(5) 
```

输出：

```bash
[11 11 23 10  5]
[10  4  4 10 10]
[11  6  9  8  4]
[24 11  4 12 16]
[ 3  7 14 17 24]
```

这里增加 `.tolist()`，可以让生成的矩阵以二维列表的形式打印，每行作为一个单独的列表

```python
# numpy 库 arange、reshape
import numpy as np


def generate_matrix(n):
    return np.arange(1, n * n + 1).reshape(n, n).tolist()
    
matrix = generate_matrix(5) 
```

```python
# numpy 库 random.randint
import numpy as np


def generate_matrix(n):
	return np.random.randint(1,n*n,size=(n,n)).tolist()
	    
matrix = generate_matrix(5) 
```

## NumPy 数组格式和标准的 Python 列表格式

1. 标准的 Python 列表格式

```bash
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
```

```bash
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
[11, 12, 13, 14, 15]
[16, 17, 18, 19, 20]
[21, 22, 23, 24, 25]
```

2. NumPy 数组格式

```bash
['[1 2 3 4 5]', '[6 7 8 9 10]', '[11 12 13 14 15]', '[16 17 18 19 20]', '[21 22 23 24 25]']
```

```bash
[1 2 3 4 5]
[ 6  7  8  9 10]
[11 12 13 14 15]
[16 17 18 19 20]
[21 22 23 24 25]
```

1. **NumPy 数组格式：** 当你直接打印一个 NumPy 数组时，它会以一种类似矩阵的格式输出，元素之间没有明确的分隔符，而是用空格或换行符进行分隔。这种格式更接近数学中矩阵的表示。
    
    示例：`[[1 2 3] [4 5 6] [7 8 9]]`
    
2. **标准的 Python 列表格式：** 当你直接打印一个 Python 列表时，它会以一种以逗号分隔的方式输出，每个子列表使用方括号括起来，元素之间用逗号分隔。
    
    示例：`[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

## 使用 列表推导和嵌套循环 生成 NumPy 数组格式

```python
def generate_matrix(n):
    return [
        "[" + " ".join(str(i + 1 + n * j) for i in range(n)) + "]" for j in range(n)
    ]


# 生成矩阵
matrix = generate_matrix(5)

# 打印矩阵
for row in matrix:
    print(row)
```

```python
def generate_matrix(n):
    result = []
    count = 1
    for i in range(n):
        row = '[' + ' '.join(str(count + j) for j in range(n)) + ']'
        count += n
        result.append(row)
    return result

# 生成矩阵
matrix = generate_matrix(5)

# 打印矩阵
for row in matrix:
    print(row)
```

### 相互转换

```python
import numpy as np

# Python 列表
python_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 转换为 NumPy 数组
numpy_array = np.array(python_list)


# 打印
print(python_list)
print("\n", numpy_array)
```

```python
import numpy as np

# NumPy 数组
numpy_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 转换为 Python 列表
python_list = numpy_array.tolist()

# 打印 
print(numpy_array)
print("\n", python_list)
```


## 数值的随机性

### 标准的 Python 列表格式

1. 列表推导
2. 嵌套循环
3. 第三方库
### NumPy 数组格式
