---
title: 帆软地图
draft: false
tags:
  - 地图
  - GIS
  - 帆软
  - finereport
---

1. 在 <https://www.poi86.com/> 下载 [连江县](https://www.poi86.com/poi/amap/district/350122/1.html) 地图数据
   连江县边界_350122_GeoJSON_(poi86.com).zip
 ![[Pasted image 20240409140210.png]]

1. 使用Python 脚本添加中心点经纬度：
   ![[Pasted image 20240409140655.png]]
 `350122.geojson` 修改文件名 `350122-area.json`

  ```python

  import json

  def calculate_center(coordinates):
  """
  计算多边形或多重多边形的中心点。
  对于多边形，计算所有点的平均值。
  对于多重多边形，对所有多边形执行相同的操作。
  """
  total_x, total_y, count = 0, 0, 0
  for part in coordinates:
   for polygon in part:
    for point in polygon:
     total_x += point[0]
     total_y += point[1]
     count += 1
  return [total_x / count, total_y / count] if count else None

  def add_centers_to_geojson(source_file_path, target_file_path):
  """
  为 GeoJSON 文件中的每个要素添加中心点。
  """
  with open(source_file_path, encoding="utf-8") as f:
   geo_data = json.load(f)

  for feature in geo_data["features"]:
   center = calculate_center(feature["geometry"]["coordinates"])
   if center:
    feature["properties"]["center"] = center

  with open(target_file_path, "w", encoding="utf-8") as f:
   json.dump(geo_data, f, ensure_ascii=False, indent=4)

  print(f"修改后的 GeoJSON 文件已保存至: {target_file_path}")

  # 使用函数处理文件

  source_file_path = "350122-area.json"
  target_file_path = "350122-modified-area.json"
  add_centers_to_geojson(source_file_path, target_file_path)
  ```
![[Pasted image 20240409142455.png]]

3. 加载资源

1. 将JSON文件放在工程webapps\webroot\WEB-INF\assets\map\image文件夹下
2. 在数据决策系统中，点击「管理系统>地图配置>同步地理文件」即可。
3. 
![[截屏2024-04-09 13.02.38.png]]

参考：[帆软的文档](https://help.fanruan.com/finereport/doc-view-2110.html)
