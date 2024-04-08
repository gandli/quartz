---
title: 使用 Python 获取卷烟信息
draft: false
tags:
  - python
  - 卷烟
---
```python
import requests
import json
import pandas as pd
# import time

base_getCigaretteListUrl = "http://sjzmjg.zm.tj.fjycyun/zm/zmglpt-case-web/cas/cig-product/getCigaretteList?menuCode=351323073100000025&page=1&limit=10834"

headers = {
    "tk": "a6095c723a2646cab2009c3ff8026932",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    # 'menuCode': '3513230731000000252',
    # 'Host': 'sjzmjg.zm.tj.fjycyun',
    # 'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN, zh;q= 0.9',
    # 'Connection': 'keep-alive',
    # 'Referer': 'http://sjzmjg.zm.tj.fjycyun/v/'
}

response = requests.get(base_getCigaretteListUrl, headers=headers)
productUuids = []

if response.status_code == 200:
    json_data = response.json()
    for item in json_data["data"]:
        productUuids.append(item["productUuid"])
else:
    print(f"请求失败，状态码：{response.status_code}")

# base_getPerfectoList = 'http://sjzmjg.zm.tj.fjycyun/zm/zmglpt-case-web/cas/cig-product/getPerfectoList?menuCode=3513230731000000252&page=1&limit=1801'

# response = requests.get(base_getPerfectoList, headers=headers)
# productUuids = []

# if response.status_code == 200:
#     json_data = response.json()
#     for item in json_data['data']:
#         productUuids.append(item['productUuid'])
# else:
#     print(f"请求失败，状态码：{response.status_code}")

base_getProductDetailsUrl = "http://sjzmjg.zm.tj.fjycyun/zm/zmglpt-case-web/cas/cig-product/getProductDetails?menuCode=351323073100000025&productUuid="
all_product_details = []

for productUuid in productUuids:
    getProductDetailsUrl = f"{base_getProductDetailsUrl}{productUuid}"
    response = requests.get(getProductDetailsUrl, headers=headers)

    if response.status_code == 200:
        detail_data = response.json()
        ProductDetail = detail_data["bean"]
        all_product_details.append(ProductDetail)
    else:
        print(f"请求失败，productUuid:{productUuid},状态码：{response.status_code}")

json_filename = "product_details.json"
with open(json_filename, "w", encoding="utf-8") as file:
    json.dump(all_product_details, file, ensure_ascii=False, indent=4)

df = pd.DataFrame(all_product_details)
xlsx_filename = "product_details.xlsx"
with pd.ExcelWriter(xlsx_filename, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False)

print(f"所有产品详细信息已保存到：{json_filename}和{xlsx_filename}")
```

```json
{
    "productName": "品规名称",
    "packType": "包装形式（条盒/软盒）",
    "brandName": "品牌名称(Rave)",
    "supplyName": "所属公司",
    "stripCode": "条装条码",
    "tarQty": "盒标焦油",
    "nicotineQty": "盒标烟碱",
    "boxCoQty": "盒标一氧化碳",
    "tbcLength": "烟支长度",
    "factoryText": "生产厂",
    "isLocSale": "销售状态",
    "supplyFully": "销售属性",
    "specsType": "创新品类",
    "productionStatus": "生产状态",
    "makeType": "工艺类型（混合型）",
    "priceType": "价类（五类烟）",
    "stripPackQty": "条盒数",
    "packQty": "盒支数",
    "wholeSalePrice": "批发价",
    "retailPrice": "零售指导价",
    "saleBeginDate": "上市时间",
    "updateDate": "更新日期",
    "enProductName": "英文名称",
    "packCode": "盒装条码",
    "productSpec": "卷烟规格",
    "imgRemark": "图片描述",
    "packaModel": "包装机型",
    "machineMarkFeature": "机型标记特征",
    "factoryMarkFeature": "生产厂标记特征"
}
```
