from flask import Flask, request, redirect, url_for, render_template_string, send_from_directory, jsonify
import os
import logging
import re
import geoip2.database
from collections import Counter
from folium import Map
from folium.plugins import HeatMap

app = Flask(__name__)
UPLOAD_FOLDER = '/root/music/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 设置日志
logging.basicConfig(filename='access.log', level=logging.INFO)

@app.route('/')
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    logging.info(f'Access from {ip}')
    with open('home.html') as f:
        return render_template_string(f.read())

@app.route('/index.html')
def index():
    with open('index.html') as f:
        return render_template_string(f.read())

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
    with open('upload.html') as f:
        return render_template_string(f.read())

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/ip')
def ip_heatmap():
    with open('map.html') as f:
        return render_template_string(f.read())

@app.route('/gen')
def ip_heatmap():
    with open('heatmap.html') as f:
        return render_template_string(f.read())

@app.route('/generate_heatmap', methods=['POST'])
def generate_heatmap():
    # 读取 access.log 文件
    with open('access.log', 'r') as file:
        log_data = file.read()

    # 查找所有 'Access from' 后面的 IP 地址
    ips = re.findall(r'Access from ([\d\.]+)', log_data)

    # 使用 GeoIP2 数据库进行 IP 地址到地理位置的转换
    reader = geoip2.database.Reader('./GeoLite2-City.mmdb')

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
    m = Map(location=[35.8617, 104.1954], zoom_start=4)
    heat_data = [[loc[0], loc[1], count] for loc, count in location_counts.items()]
    HeatMap(heat_data).add_to(m)
    m.save('map.html')

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
