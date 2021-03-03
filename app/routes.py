from flask import render_template, url_for, request
from app import app
from app import db
import pprint



@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/getstarted')
def getstarted(method="POST"):
   collection = db.template
   return render_template('getstarted.html')

