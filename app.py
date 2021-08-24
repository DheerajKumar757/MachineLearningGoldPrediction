# importing libraries
import pickle
import numpy
from flask import Flask, request, render_template

# Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('gld_value.pkl', 'rb'))

# user defined function
@app.route('/', methods= ['GET'])
def Home():
    return render_template('gold_value.html')

@app.route('/prediction', methods= ['POST'])
def predict():
    spx = int(request.form['spx'])
    uso = int(request.form['uso'])
    slv = int(request.form['slv'])
    usd = int(request.form['usd'])
    prediction = loadedModel.predict([[spx, uso, slv, usd]])

    return render_template('gold_value.html', gold_output= prediction, Spx= spx, Uso=uso, Slv=slv, Usd= usd)



app.run(debug=True)