from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/getstarted')
def getstarted(method="POST"):
   return render_template('getstarted.html')

