from flask import Flask, request, render_template, url_for
from .thermo import *
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/data', methods = ['POST', 'GET'])
def data():
    url_for('static', filename='style.css')
    if request.method == 'POST':
        material = request.form['material'].lower()
        Temp = int(request.form['Temp'])
    else:
        material = request.args.get('material')
        Temp = int(request.args.get('Temp'))
    data = getThermoData(material, Temp)
    return data 