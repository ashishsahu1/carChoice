from flask import Flask, render_template, request
from flask import jsonify
import pickle

modelUrl = open('random_forest_regression_model.pkl', 'rb')
model = pickle.load(modelUrl)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

data =[]

@app.route('/predict', methods =["POST","GET"])
def predict():    
    if request.method == 'POST':
        name = str(request.form['name'])
        marketprice = float(request.form["marketPrice"])
        distance = int(request.form["distance"])
        age = int(request.form["age"])
        owner = int(request.form["lastOwner"])
        fuel = str(request.form["fuel"])
        trans = str(request.form["trans"])
        seller = str(request.form["seller"])

        if trans=='auto':
            trans = 0
        else:
            trans = 1

        if seller=='dealer':
            transm = 0
        else:
            transm = 1

        data=[[marketprice, distance, owner, age,]]

        return render_template('index.html', n=name, m =marketprice,
                            d = distance, a =age, o = owner, f=fuel, t=trans,
                            s=seller)
    return 'something went wrong'



if __name__ == "__main__":
    app.run(debug = True)