from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods =["POST","GET"])
def predict():    
    if request.method == 'POST':
        name = str(request.form['name'])
    # name = request.form.get("name") 
    # marketprice = request.form.get("marketPrice") 
    # distance = request.form.get("distance") 
    # age = request.form.get("age") 
        return render_template('index.html', n = name)
    return 'something went wrong'

# @app.route('/res', methods =["GET", "POST"])
# def result():
#     return str(name)

@app.route('/api', methods =["GET", "POST"])
def api():
    return jsonify({'name':'Jimit','address':'India'})

if __name__ == "__main__":
    app.run(debug = True)