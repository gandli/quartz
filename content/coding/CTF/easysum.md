---
title: easysum 数表求最大乘积
draft: false
tags:
  - python
  - 题目
  - 矩阵
  - OCR
  - CTF
  - 数表
  - 乘积
date: 2024-04-27
---
## 1. 访问题目

![[Pasted image 20240427154408.png]]
![[Pasted image 20240427154414.png]]
![[Pasted image 20240427154420.png]]

> 你拿到了一个`15*15`的数表，请你求得数表中在一条线上（行、列、两个对角线）连续5个数的乘积的最大值，并将这5个数的10个数字按数字从小到大从左到右排列形成密码串，并分别提交。
>
## 2. 编写 `easysum_exp.py`

python 3下安装依赖`pip install pytesseract pillow`

```python
from PIL import Image, ImageEnhance  # pip install Pillow
import pytesseract  # pip install pytesseract
import re


# 定义函数,识别数表图片为二维数组列表
def image_to_matrix(image_path):
    # 打开并增强图像
    image = Image.open(image_path)
    image = ImageEnhance.Contrast(image).enhance(1.5).resize((1024, 768))

    # 使用 pytesseract 提取文本
    custom_config = r"--oem 3 --psm 6"
    text = pytesseract.image_to_string(image, config=custom_config)

    # 过滤不需要的字符
    filter_text = re.sub(r"[^\d\s]", "", text)

    # 将文本转换为矩阵
    matrix = [list(map(int, line.split())) for line in filter_text.strip().split("\n")]
    return matrix


# 定义函数找到序列的最大乘积
def find_max_prod(matrix, n):
    row_len, col_len = len(matrix), len(matrix[0])
    max_product = 0
    max_sequence = []

    for row in range(row_len):
        for col in range(col_len):
            # 检查所有四个可能的方向
            directions = [
                (0, 1),  # 水平
                (1, 0),  # 垂直
                (1, 1),  # 对角
                (1, -1),  # 反对角
            ]
            for dr, dc in directions:
                if (
                    0 <= col + dc * (n - 1) < col_len
                    and 0 <= row + dr * (n - 1) < row_len
                ):
                    product = 1
                    sequence = [matrix[row + i * dr][col + i * dc] for i in range(n)]
                    for num in sequence:
                        product *= num
                    if product > max_product:
                        max_product = product
                        max_sequence = sequence

    return max_sequence, max_product


# 数表图片转二维数组列表
matrix = image_to_matrix("file.jpg")

# 获取一条线上5个数的最大乘积和序列
max_sequence, max_product = find_max_prod(matrix, 5)

# 打印结果
print("最大乘积:", max_product)
print("具有最大乘积的序列:", max_sequence)
print("序列按照数字升序:", "".join(sorted("".join(map(str, max_sequence)))))
```
