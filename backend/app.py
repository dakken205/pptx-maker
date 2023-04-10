from flask import Flask, render_template, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__, static_folder="./../frontend/dist/static", template_folder="./../frontend/dist")

app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")
