---
title: 数表求最大乘积
draft: false
tags:
  - python
  - 题目
  - 矩阵
  - OCR
  - CTF
date: 2024-04-27
---
## 1. 访问题目

![[Pasted image 20240427154408.png]]
![[Pasted image 20240427154414.png]]
![[Pasted image 20240427154420.png]]


> 你拿到了一个`15*15`的数表，请你求得数表中在一条线上（行、列、两个对角线）连续5个数的乘积的最大值，并将这5个数的10个数字按数字从小到大从左到右排列形成密码串，并分别提交。
## 2. 编写 `easysum_exp.py`

python 3下安装依赖`pip install pytesseract pillow`

```python
import pytesseract
from PIL import Image, ImageEnhance

# 打开图像文件
img = Image.open("file-easysum/file.jpg")

# 增强图像对比度，使文本更清晰
enhancer = ImageEnhance.Contrast(img)
img_enhanced = enhancer.enhance(1.5)  # 调整对比度的级别

# 调整图像大小并应用阈值过滤器进行二值化处理
img_resized = img_enhanced.resize((1024, 768))
img_binarized = img_resized.convert("L").point(lambda x: 0 if x < 128 else 255, "1")

# 配置 Tesseract 以将图像视为单一块文本
custom_config = r"--oem 3 --psm 6"
text = pytesseract.image_to_string(img_binarized, config=custom_config)

# 替换识别结果中的度数符号为一个空格
text = text.replace("°", " ")
# print(text)


# 处理识别的文本，将其转换为二维数组
def convert_text_to_matrix(text):
    # 根据换行符分割文本为多行
    lines = text.strip().split("\n")

    # 初始化二维数组
    matrix = []
    for line in lines:
        # 过滤掉非数字字符，并以空格分割每一行中的数字
        numbers = line.strip().split()
        # 将字符串中的数字转换为整数列表
        number_list = [int(num) for num in numbers if num.isdigit()]
        # 如果列表非空，则添加到二维数组中
        if number_list:
            matrix.append(number_list)

    return matrix


# 调用函数，将文本转换为二维数组
matrix = convert_text_to_matrix(text)

# 打印转换后的二维数组
print("矩阵：")
for row in matrix:
    print(row)


def find_max_product(matrix, length):
    all_sequences = []

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if j + length <= cols:  # 检查水平方向
                all_sequences.append(matrix[i][j : j + length])

            if i + length <= rows:  # 检查垂直方向
                all_sequences.append([matrix[i + k][j] for k in range(length)])

            if i + length <= rows and j + length <= cols:  # 检查主对角线方向
                all_sequences.append([matrix[i + k][j + k] for k in range(length)])

            if i - length + 1 >= 0 and j + length <= cols:  # 检查副对角线方向
                all_sequences.append([matrix[i - k][j + k] for k in range(length)])

    all_products = []
    for sequence in all_sequences:
        product = 1
        for number in sequence:
            product *= number
        all_products.append(product)

    max_product = max(all_products, default=0)
    max_index = all_products.index(max_product)

    return {
        "all_sequences": all_sequences,
        "all_products": all_products,
        "max_product": max_product,
        "index": max_index + 1,
        "sequence": all_sequences[max_index],
    }


result = find_max_product(matrix, 5)
# print(f"\n长度为 {5} 的最大乘积分析：")
# print("所有序列：")
# for seq in result["all_sequences"]:
#     print(seq)
# print("\n所有乘积：", result["all_products"])
# print("\n最大乘积值：", result["max_product"])
# print("最大乘积索引：", result["index"])
# print("产生最大乘积的序列：", result["sequence"])
print("\nMAX  SUM:", result["max_product"])
print("PassWord:", "".join(sorted("".join(map(str, result["sequence"])))))
```

### 输出：

```bash
矩阵：
[71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33]
[60, 99, 13, 45, 22, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17]
[28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38]
[68, 32, 62, 12, 20, 95, 63, 94, 39, 63, 68, 40, 91, 66, 49]
[25, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89]
[89, 75, 10, 76, 44, 20, 45, 35, 14, 30, 61, 33, 97, 34, 31]
[28, 22, 75, 31, 67, 15, 94, 63, 80, 44, 62, 16, 14, 79, 53]
[42, 96, 35, 31, 47, 55, 58, 88, 24, 70, 17, 54, 24, 36, 29]
[48, 35, 71, 89, 67, 95, 54, 61, 37, 44, 60, 21, 58, 51, 54]
[68, 15, 64, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 34, 89]
[83, 90, 35, 90, 16, 87, 97, 57, 32, 16, 26, 26, 79, 33, 27]
[87, 57, 62, 20, 72, 23, 46, 33, 67, 46, 55, 12, 32, 63, 93]
[73, 38, 25, 39, 11, 24, 94, 72, 18, 58, 46, 29, 32, 40, 62]
[41, 72, 30, 23, 88, 34, 62, 92, 69, 82, 67, 59, 85, 74, 84]
[29, 78, 31, 90, 31, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57]

MAX  SUM: 2171903490
PassWord: 1455677899
```