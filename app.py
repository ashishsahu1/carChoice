from flask import Flask, render_template, request
from flask import jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

data =[]

@app.route('/predict', methods =["POST","GET"])
def predict():    
    if request.method == 'POST':
        modelUrl = open('random_forest_regression_model.pkl', 'rb')
        model = pickle.load(modelUrl)
        name = str(request.form['name'])
        marketprice = float(request.form["marketPrice"])
        distance = int(request.form["distance"])
        age = int(request.form["age"])
        owner = int(request.form["lastOwner"])
        fuel = str(request.form["fuel"])
        trans = str(request.form["trans"])
        seller = str(request.form["seller"])
        fp = 0
        fd = 0
        if trans=='auto':
            trans = 0
        else:
            trans = 1

        if seller=='dealer':
            seller = 0
        else:
            seller = 1
        
        if fuel == 'Petrol':
            fp=1
        elif fuel == 'Diesel':
            fd=1
        else:
            fp=0
            fd=0


        data=[[marketprice, distance, owner, age,fd,fp,seller,trans]]
        result = model.predict(data)
        x = round(result[0],2)

        if x<0:
            final = "Sorry to say "+str(name)+", you can not buy this car 🙁 "

        final = str(name)+", this car would cost you around Rs "+str(x)+" Lakhs"

        return render_template('index.html', f=final)
    return 'something went wrong'



if __name__ == "__main__":
    app.run(debug = True)