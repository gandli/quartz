---
title: python 矩阵研究
draft: false
tags:
  - python
  - 矩阵
  - 编程
  - 随机数
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

## `range(start, stop)` 和 `np.arange(start, stop)`

`range(start, stop)` 和 `np.arange(start, stop)` 都是用来生成一个连续整数序列的，但它们来自不同的库并且有一些细微的差别。下面是它们的基本用法和取值范围的详细解释：

### `range(start, stop)`

`range()` 是 Python 内置的函数，用于生成一个不可变的序列类型，这个序列通常用于循环中。`range()` 生成的是一个迭代器，它不会立即分配内存来存储整个数列。

- **start**：序列的起始值，包含在序列中。
- **stop**：序列的结束值，不包含在序列中。
- **step**（可选）：序列中每个数之间的间隔，默认为1。

`range()` 只能用于生成整数序列。

### `np.arange(start, stop, [step, dtype])`

`np.arange()` 是 `NumPy` 库中的函数，它返回一个数组，而不是一个迭代器。这意味着 `np.arange()` 会立即分配内存来存储整个数列。

- **start**：序列的起始值，包含在数组中。
- **stop**：序列的结束值，不包含在数组中。
- **step**（可选）：序列中每个数之间的间隔，默认为1。
- **dtype**（可选）：数组的数据类型。如果指定，可以定义生成的数组中元素的数据类型，例如 `np.float32`。

与 `range()` 不同的是，`np.arange()` 可以生成浮点数序列。这是一个重要的功能，特别是在需要非整数步长或处理数值计算时。

### 示例

**使用 `range()` 生成整数序列：**

```python
for i in range(1, 10):
    print(i, end=' ')  # 输出 1 2 3 4 5 6 7 8 9
```

**使用 `np.arange()` 生成浮点数序列：**

```python
import numpy as np
arr = np.arange(0.5, 5.5, 0.5)
print(arr)  # 输出 [0.5 1.  1.5  2.  2.5 3.  3.5 4.  4.5 5. ]
```

选择 `range()` 还是 `np.arange()` 取决于具体的使用场景。如果你需要高性能的数组操作，特别是在科学计算中，`np.arange()` 更加适合。而对于基本的迭代需求，`range()` 更加简单且内存效率更高。

## 使用 `random` 生成一个随机数

在 Python 中生成随机数可以通过标准库中的 `random` 模块来实现。这个模块提供了生成随机数的多种方法，适用于不同的需求。下面是一些常用的功能及其用法：

### 1. 生成一个随机浮点数

使用 `random.random()` 可以生成一个 [0.0, 1.0) 范围内的随机浮点数，包括 0.0 但不包括 1.0。

```python
import random
num = random.random()
print(num)
```

### 2. 生成一个指定范围内的随机整数

`random.randint(a, b)` 生成一个 [a, b] 范围内的随机整数，包括两端的 a 和 b。

```python
import random
num = random.randint(1, 10)  # 生成 1 到 10 之间的随机整数（包括 1 和 10）
print(num)
```

### 3. 生成一个指定范围和步长的随机整数

使用 `random.randrange(start, stop[, step])` 可以生成一个从 `start` 到 `stop` 的随机整数，可以指定步长 `step`。注意 `stop` 是不包括的。

```python
import random
num = random.randrange(0, 101, 5)  # 生成 0 到 100 之间，步长为 5 的随机整数（如 0, 5, 10, ..., 95, 100）
print(num)
```

### 4. 随机选择列表中的元素

`random.choice(sequence)` 从非空序列中随机选择一个元素。

```python
import random
items = [1, 2, 3, 4, 5]
selected_item = random.choice(items)
print(selected_item)
```

### 5. 打乱列表顺序

`random.shuffle(x)` 用于将列表中的元素随机打乱。

```python
import random
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)
```

### 6. 生成一个随机浮点数，指定范围

`random.uniform(a, b)` 生成一个 [a, b] 或 [b, a] 范围内的随机浮点数，包括两端的 a 和 b。

```python
import random
num = random.uniform(1.0, 10.0)
print(num)
```

这些方法覆盖了大部分生成随机数的常见需求。通过使用 `random` 模块，你可以轻松实现各种随机数据生成的功能。

### 使用 列表推导 生成随机的数组矩阵

```python
import random


def generate_list_array(n, lower=1, upper=100):
    # 为 py_list 生成随机数
    py_list = [[random.randint(lower, upper) for _ in range(n)] for _ in range(n)]

    # 为 np_array 生成随机数
    np_array = [
        "[" + " ".join(str(random.randint(lower, upper)) for _ in range(n)) + "]"
        for _ in range(n)
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

打印：

```bash
标准的 Python 列表格式:
[41, 29, 24, 88, 14]
[50, 9, 28, 42, 38]
[86, 52, 22, 79, 13]
[59, 67, 23, 62, 85]
[71, 7, 16, 57, 69]

NumPy 数组格式:
[46 9 66 97 24]
[2 42 33 31 56]
[12 20 79 48 74]
[30 31 7 33 37]
[69 83 19 80 96]
```

### 使用 嵌套循环 生成随机的数组矩阵

```python
import random

def generate_list_array(n, lower=1, upper=100):
    py_list = []
    np_array = []

    # 使用嵌套循环为 py_list 生成随机数
    for i in range(n):
        py_row = []
        for j in range(n):
            value = random.randint(lower, upper)
            py_row.append(value)
        py_list.append(py_row)

    # 使用嵌套循环独立地为 np_array 生成随机数，并立即格式化为字符串
    for i in range(n):
        np_row = []
        for j in range(n):
            value = random.randint(lower, upper)
            np_row.append(str(value))
        formatted_row = "[" + " ".join(np_row) + "]"
        np_array.append(formatted_row)

    return py_list, np_array

py_list, np_array = generate_list_array(5)

print("标准的 Python 列表格式:")
for row in py_list:
    print(row)
print("\nNumPy 数组格式:")
for row in np_array:
    print(row)
```

打印：

```bash
标准的 Python 列表格式:
[18, 59, 48, 68, 96]
[39, 93, 30, 52, 58]
[94, 25, 19, 73, 30]
[1, 3, 24, 65, 3]
[87, 51, 30, 81, 100]

NumPy 数组格式:
[76 12 24 86 84]
[83 71 42 12 72]
[72 9 86 80 51]
[36 9 47 76 67]
[95 50 76 61 45]
```

### 使用 `numpy` 生成随机的数组矩阵

```python
import numpy as np

def generate_list_array(n, lower=1, upper=100):
    # 使用 NumPy 生成 py_list 的随机矩阵
    py_array = np.random.randint(lower, upper + 1, size=(n, n))
    py_list = py_array.tolist()

    # 使用 NumPy 生成 np_array 的随机矩阵，并格式化为字符串列表
    np_random_array = np.random.randint(lower, upper + 1, size=(n, n))
    np_array = ["[" + " ".join(map(str, row)) + "]" for row in np_random_array]

    return py_list, np_array

py_list, np_array = generate_list_array(5)

print("标准的 Python 列表格式:")
for row in py_list:
    print(row)
print("\nNumPy 数组格式:")
for row in np_array:
    print(row)
```

打印：

```bash
标准的 Python 列表格式:
[72, 68, 84, 89, 16]
[84, 91, 30, 59, 26]
[4, 46, 43, 73, 60]
[18, 56, 66, 61, 77]
[94, 24, 54, 64, 6]

NumPy 数组格式:
[50 72 46 78 87]
[15 62 84 44 73]
[74 1 47 90 22]
[41 32 17 21 68]
[9 83 82 39 71]
```
