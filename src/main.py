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
    app.run(debug=True)
    model = Model()

    model.setURL("https://identity.getpostman.com/client-auth/confirm?auth_challenge=1fd0b6148302fa77e402a261450956b54bdada170bdb7b3ac7f74d7884d582ca&auth_device=app_native&auth_device_version=10.24.3")
    x = np.array(model.getFeature()).reshape(1,-1)


    print(model.predicts(x))

