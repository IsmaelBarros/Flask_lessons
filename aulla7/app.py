import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
print(os.getcwd(), flush=True)
app = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'aulla7\\upload')
print(UPLOAD_FOLDER, flush=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return 'Upload com sucesso.'


@app.route('/get-file/<filename>')
def get_file(filename):
    file = os.path.join(UPLOAD_FOLDER, filename + '.jpeg')
    return send_file(file, mimetype='imagem/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
