from flask import Flask, request, render_template, url_for
from .thermo import *
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
        material = request.form['material'].lower()
        Temp = int(request.form['Temp'])
    else:
        material = request.args.get('material')
        Temp = int(request.args.get('Temp'))
    data = getThermoData(material, Temp)
    return data 

if __name__ == "__main__":
    app.run()

