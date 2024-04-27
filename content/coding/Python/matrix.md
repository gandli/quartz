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
# matrix = [[i + 1 + 5 * j for i in range(5)] for j in range(5)]
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
    # result = [[i + 1 + n * j for i in range(n)] for j in range(n)]
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

### 标准的 Python 列表格式和NumPy 数组格式

1. 列表推导
```python
# 列表推导
def generate_list_array(n):
    py_list = [[i + 1 + n * j for i in range(n)] for j in range(n)]

    np_array = [
        "[" + " ".join(str(i + 1 + n * j) for i in range(n)) + "]" for j in range(n)
    ]

    return py_list, np_array


py_list, np_array = generate_list_array(5)

print("标准的 Python 列表格式:")
for row in py_list:
    print(row)
print("\nNumPy 数组格式:")
for row in np_array:
    print(row)
```
1. 嵌套循环
```python
# 嵌套循环
def generate_list_array(n):
    py_list = []
    np_array = []

    for i in range(n):
        py_row = []
        np_row = []
        for j in range(n):
            # 直接计算当前元素的值并添加到行列表中
            value = i * n + j + 1
            py_row.append(value)
            np_row.append(str(value))
        py_list.append(py_row)
        np_array.append("[" + " ".join(np_row) + "]")
    return py_list, np_array


py_list, np_array = generate_list_array(5)

print("标准的 Python 列表格式:")
for row in py_list:
    print(row)
print("\nNumPy 数组格式:")
for row in np_array:
    print(row)
```
3. 第三方库

```python
import numpy as np

def generate_list_array(n):
    # 使用 NumPy 的 arange 函数生成连续元素，并调整形状为 n x n
    np_array = np.arange(1, n*n + 1).reshape(n, n)

    # 将 NumPy 数组转换为 Python 列表，以符合原函数的返回类型
    py_list = np_array.tolist()

    # 格式化为 NumPy 数组格式的字符串（模拟你的原函数输出）
    formatted_np_array = ["[" + " ".join(map(str, row)) + "]" for row in np_array]

    return py_list, formatted_np_array

# 调用函数
py_list, formatted_np_array = generate_list_array(5)

print("标准的 Python 列表格式:")
for row in py_list:
    print(row)
print("\nNumPy 数组格式:")
for row in formatted_np_array:
    print(row)
```