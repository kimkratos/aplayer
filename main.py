from flask import Flask, request, redirect, url_for, render_template_string, send_from_directory
import os
import logging

app = Flask(__name__, static_url_path='/2048', static_folder='2048', template_folder='2048')
UPLOAD_FOLDER = '/root/music/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 设置日志
logging.basicConfig(filename='access.log', level=logging.INFO)


@app.route('/2048')
def game():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    logging.info(f'Access from {ip}')
    with open('2048.html') as f:
        return render_template_string(f.read())
        
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
