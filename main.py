import pymongo as pymongo
from flask import Flask, request, jsonify
from flask_objectid_converter import ObjectIDConverter
from pymongo import ReturnDocument
from pymongo.server_api import ServerApi
from bson import json_util, ObjectId
from flask_cors import CORS
import datetime as dt


from dotenv import load_dotenv

load_dotenv()
import os

MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGO_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")

#connecting to mongodb
client = pymongo.MongoClient(f"mongodb+srv: //{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority",
                             server_api=ServerApi('1'))

db = client.sound

def getTimeStamp():
    return dt.datetime.today().replace(microsecond=0)

app = Flask(__name__)

app.url_map.converters['objectid'] = ObjectIDConverter

app.config['DEBUG'] = True

CORS(app)



