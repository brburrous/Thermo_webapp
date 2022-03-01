from flask import Flask, request, render_template
from .thermo import getThermoData
 
app = Flask(__name__)
 
@app.route('/')
def index():
    foo() 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)