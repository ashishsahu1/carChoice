from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def predict():
    if request.method == "POST":
        name = request.form.get("name") 
        marketprice = request.form.get("marketPrice") 
        distance = request.form.get("distance") 
        age = request.form.get("age") 
        return name+" "+marketprice+" "+distance+" "+age
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)