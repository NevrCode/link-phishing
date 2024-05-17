from model import Model
import numpy as np
from flask import jsonify, Flask, request 


app = Flask(__name__)

@app.route("/")
def home() :
    return "Home"

@app.route("/input-link", methods=['POST'])
def post_input() :
    data = request.get_json()
    
    model = Model()

    model.setURL(data['link'])
    x = np.array(model.getFeature()).reshape(1,-1)
    result = model.predicts(x)
    
    res = {
        'result' : "Phishing" if result == 1 else "The Link is Safe"
    }

    return jsonify(res), 201




if __name__ == "__main__" :
    app.run(host='0.0.0.0',port=5000)


