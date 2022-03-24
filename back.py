from ctypes import util
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import sys
# problema com o arquivo grande
sys.setrecursionlimit(3000)
app = Flask(__name__)
CORS(app)

util = None

app.config['UPLOAD_PATH'] = 'files'

@app.route('/start', methods=['POST'])
def upload_file():
    global util
    uploaded_file = request.files['file']
    bucketSize = request.form.get("bucketSize")
    pageSize = request.form.get("pageSize")
    f = open("pageBucketSize.py", "w")
    f.write(f'bucketSize={bucketSize}\npageSize={pageSize}')
    f.close()
    filename = secure_filename(uploaded_file.filename)
    file = None
    if filename != '':
        uploaded_file.save(filename)
        file = os.path.join(filename)

    if file is not None:
        from util import Util
        util = Util()
        util.readFile(file)
    return jsonify(status="ok")

@app.route('/info', methods=['GET'])
def get_info():
    if util is None:
        return jsonify(status="error")
    return jsonify(util.ver())

@app.route('/search', methods=['POST'])
def search():
    if util is None:
        return jsonify(status="error")
    query = request.args.get('query')
    
    steps = util.busca(query)[0]
    return jsonify(custo=steps)

@app.route('/coisa', methods=['POST'])
def coisa():
    return request.get_json()

if __name__ == '__main__':
    app.run()