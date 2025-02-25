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
