from flask import Flask, request, jsonify
from flask_cors import CORS

from pro import clean_text_using_nlp

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def hello():
    
    data = request.json
    text = data['clean_data']
    
    clean_data = clean_text_using_nlp(text)

    return jsonify({"clean_data": clean_data})
    

if __name__ == '__main__':
    app.run(debug=True)
