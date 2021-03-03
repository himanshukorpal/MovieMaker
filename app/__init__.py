from flask import Flask
from config import Config
from pymongo import MongoClient
app = Flask(__name__)
app.config.from_object(Config)
client = MongoClient("mongodb://localhost:27017/")
db = client.moviemaker
# collection = db.template
# template = db.template
# temp = video_templates
# template.insert_many([temp])



from app import routes


