from http.client import responses

from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app= Flask(__name__)
CORS(app)

@app.route('/classify_image', methods=['GET','POST'])
def classify_image():
    image_data=request.form['image_data']
    response= jsonify(util.classify_image(image_data,None))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(port=5000)