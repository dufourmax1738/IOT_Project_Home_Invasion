import pymongo as pymongo
from flask import Flask, request, jsonify
from flask_objectid_converter import ObjectIDConverter
from pymongo import ReturnDocument
from pymongo.server_api import ServerApi
from bson import json_util, ObjectId
from flask_cors import CORS
import datetime as dt
from IOT_Project_Home_Invasion.Schemas import MotionSensorSchema

from dotenv import load_dotenv



load_dotenv()
import os

MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGO_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")

#connecting to mongodb
client = pymongo.MongoClient(f"mongodb+srv: //{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority",
                             server_api=ServerApi('1'))

db = client.motion

if 'motion' not in db.list_collections_names():
    db.create_collection("motion detected",
                         timeseries={'timeField': 'timestamp', 'metaField': 'sensorId', 'granularity': 'hours'})


def getTimeStamp():
    return dt.datetime.today().replace(minute=1)

app = Flask(__name__)

app.url_map.converters['objectid'] = ObjectIDConverter

app.config['DEBUG'] = True

#mkaing our api accessible by any IP
CORS(app)

@app.route("/sensors/<int:sensorId>/motion", methods=["POST"])
def add_motion_value(sensorId):
    error = MotionSensorSchema().validate(request.json)
    if error:
        return error, 400

    data = request.json
    data.update({"timestamp": getTimeStamp(), "sensorId": sensorId})

    db.motion.insert_one(data)

    data["_id"] = str(data["_id"])
    data["timestamp"] = data["timestamp"].strftime("%Y-%m-%dT%H:%M:%S")
    return data

@app.route("/sensors/<int:sensorId>/motion")
def get_all_motion(sensorId):
    start = request.args.get("start")
    end = request.args.get("end")

    query = {"sensorId": sensorId}
    if start is None and end is not None:
        try:
            end = dt.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")
        except Exception as e:
            return {"error": "timestamp not following format %Y-%m-%dT%H:%M:%S"}, 400

        query.update({"timestamp": {"$lte": end}})

    elif end is None and start is not None:
        try:
            start = dt.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
        except Exception as e:
            return {"error": "timestamp not following format %Y-%m-%dT%H:%M:%S"}, 400

        query






