from flask import Flask, request, render_template
from .test import foo
 
app = Flask(__name__)
 
@app.route('/')
def index():
    foo() 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)