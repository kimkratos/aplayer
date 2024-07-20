import re
import geoip2.database
import folium
from collections import Counter
from folium.plugins import HeatMap

# 读取 access.log 文件
with open('access.log', 'r') as file:
    log_data = file.read()

# 查找所有 'Access from' 后面的 IP 地址
ips = re.findall(r'Access from ([\d\.]+)', log_data)

# 使用 GeoIP2 数据库进行 IP 地址到地理位置的转换
reader = geoip2.database.Reader('/mnt/data/GeoLite2-City.mmdb')

locations = []
for ip in ips:
    try:
        response = reader.city(ip)
        locations.append((response.location.latitude, response.location.longitude))
    except geoip2.errors.AddressNotFoundError:
        continue

# 统计每个地理位置的出现次数
location_counts = Counter(locations)

# 生成热力图
m = folium.Map(location=[35.8617, 104.1954], zoom_start=4)
heat_data = [[loc[0], loc[1], count] for loc, count in location_counts.items()]
HeatMap(heat_data).add_to(m)
m.save('templates/heatmap.html')
