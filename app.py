from flask import Flask, request, render_template, send_file, redirect, url_for, jsonify
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'jfif', 'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    target_format = request.form.get('format', 'png')  
    files = request.files.getlist('file')
    if not files or files[0].filename == '':
        return jsonify({'error': 'No file uploaded'}), 400
    converted_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            img = Image.open(filepath)
            new_filename = filename.rsplit('.', 1)[0] + '.' + target_format
            new_filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
            img.save(new_filepath)
            converted_files.append(new_filename)
    return jsonify({'files': converted_files})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
