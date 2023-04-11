from flask import Flask, render_template, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__, static_folder="./../frontend/dist/static", template_folder="./../frontend/dist")

app.config['JSON_AS_ASCII'] = False
# CORS(app)
CORS(app, resources={r"/*": {"origins": ["http://localhost:8080"]}})

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

@app.route('/download', methods=['POST'])
def download():
    try:
        if request.method == 'POST':
            data = request.get_json()
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'result' : 'Invalid method.'}))
    except:
        return make_response(jsonify({'result' : 'Something error occured in server.'}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
