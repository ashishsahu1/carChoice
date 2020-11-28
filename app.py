from flask import Flask, render_template, request
from flask import jsonify
import pickle

modelUrl = open('random_forest_regression_model.pkl', 'rb')
model = pickle.load(modelUrl)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
# render_template('index.html', n = name)
@app.route('/predict', methods =["POST","GET"])
def predict():    
    if request.method == 'POST':
        name = str(request.form['name'])
        marketprice = float(request.form["marketPrice"])
        distance = int(request.form["distance"])
        age = int(request.form["age"])
        owner = int(request.form["lastOwner"])










        return render_template('index.html', predict = pred)
    return 'something went wrong'



if __name__ == "__main__":
    app.run(debug = True)