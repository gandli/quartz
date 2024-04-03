---
title: 使用 Python 查找勾股数
draft: false
tags:
  - 勾股数
---
```python
 def find_pythagorean_triples():
    results = []
    # 遍历可能的a和b的组合
    for a in range(1, 1000):  # a的上限设置为999，即最大的3位数
        for b in range(a, 1000):  # b从a开始遍历，确保a < b
            c = (a**2 + b**2)**0.5
            if c.is_integer() and len(str(a) + str(b) + str(int(c))) == 6:
                results.append((a, b, int(c)))
                # 当找到一组符合条件的组合时，打印出来
                print(f"找到勾股数组合: {a}, {b}, {int(c)}")
    return results

# 调用函数并捕获结果
pythagorean_triples = find_pythagorean_triples()
if not pythagorean_triples:
    print("没有找到符合条件的勾股数组合。")
```
