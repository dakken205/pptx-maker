from flask import Flask, render_template, jsonify, request, make_response, send_file
from flask_cors import CORS
from pp_edit_python_test import *
from pptx import Presentation
from pptx.util import Inches
import io

app = Flask(__name__, static_folder="./../frontend/dist/static", template_folder="./../frontend/dist")

app.config['JSON_AS_ASCII'] = False
CORS(app)
# CORS(app, resources={r"/*": {"origins": ["http://localhost:8080"]}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    # try:
        if request.method == 'POST':
            data = request.get_json()
            hasInfo = bool(len(data['info_contents']))

            prs = Presentation()
            prs.slide_width = Inches(16 * 5 / 6)
            prs.slide_height = Inches(9 * 5 / 6)

            add_start_slide(prs, data['datefmt'])
            add_outline_slide(prs, hasInfo)
            add_department_slide(prs, data['departments_contents'])
            add_info_share(prs, data['info_contents'])
            
            # powerpointファイルをメモリ上に保存する
            ppt_file = io.BytesIO()
            prs.save(ppt_file)
            
            # ダウンロード用URLを返す
            download_url = request.host_url + 'download'
            return jsonify({'download_url': download_url})
        else:
            return make_response(jsonify({'result' : 'Invalid method.'}))
    # except:
        # return make_response(jsonify({'result' : 'Something error occured in server.'}))

@app.route('/download', methods=['POST'])
def download_ppt():
    # PowerPointファイルをダウンロードする
    ppt_file = generate()
    return send_file(ppt_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
