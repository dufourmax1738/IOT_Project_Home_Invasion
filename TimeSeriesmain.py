import pymongo as pymongo
import emulator as em
from flask import Flask, request, jsonify
from flask_objectid_converter import ObjectIDConverter
from pymongo import ReturnDocument
from pymongo.server_api import ServerApi
from Schemas import SoundSensorSchema, MotionSensorSchema
from bson import json_util, ObjectId
from flask_cors import CORS
import datetime as dt


# loading private connection information from environment variables
from dotenv import load_dotenv

load_dotenv()
import os

MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")

# connecting to mongodb
client = pymongo.MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority",
                             server_api=ServerApi('1'))

db = client.HomeInvasions

# mongodb+srv://<username>:<password>@iotfinalproject.ldavcfn.mongodb.net/?retryWrites=true&w=majority

if 'sound' not in db.list_collection_names():
    db.create_collection("sound",
                         timeseries={'timeField': 'timestamp', 'metaField': 'sensorId', 'granularity': 'hours'})

if 'motion' not in db.list_collection_names():
    db.create_collection("motion",
                         timeseries={'timeField': 'timestamp', 'metaField': 'sensorId', 'granularity': 'hours'})

em.postSound()
em.postMotion()

def getTimeStamp():
    return dt.datetime.today().replace(microsecond=0)


app = Flask(__name__)
# adding an objectid type for the URL fields instead of treating it as string
# this is coming from a library we are using instead of building our own custom type
app.url_map.converters['objectid'] = ObjectIDConverter

app.config['DEBUG'] = True
# making our API accessible by any IP
CORS(app)


@app.route("/sensors/<int:sensorId>/sound", methods=["POST"])
def add_sound_value(sensorId):
    error = SoundSensorSchema().validate(request.json)
    if error:
        return error, 400

    data = request.json
    data.update({"timestamp": getTimeStamp(), "sensorId": sensorId})

    db.sound.insert_one(data)

    data["_id"] = str(data["_id"])
    data["timestamp"] = data["timestamp"].strftime("%Y-%m-%dT%H:%M:%S")
    return data


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
def get_sensor_motion(sensorId):
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

        query.update({"timestamp": {"$gte": start}})

    elif start is not None and end is not None:
        try:
            start = dt.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
            end = dt.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")

        except Exception as e:
            return {"error": "timestamp not following format %Y-%m-%dT%H:%M:%S"}, 400

        query.update({"timestamp": {"$gte": start, "$lte": end}})

    data = list(db.motion.aggregate([
        {
            '$match': query
        }, {
            '$group': {
                '_id': '$sensorId',
                'motionCount': {
                    '$count': {}
                },
                'motion': {
                    '$push': {
                        'timestamp': '$timestamp',
                        'motion': '$motion'
                    }
                }

            }
        }
    ]))

    if data:
        data = data[0]
        if "_id" in data:
            del data["_id"]
            data.update({"sensorId": sensorId})

        for motion in data['motion']:
            motion["timestamp"] = motion["timestamp"].strtime("%Y-%m-%dT%H:%M:%S")

        return data
    else:
        return {"error": "id not found"}, 404


@app.route("/sensors/<int:sensorId>/sound")
def get_sensor_sound(sensorId):
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

        query.update({"timestamp": {"$gte": start}})
    elif start is not None and end is not None:
        try:
            start = dt.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
            end = dt.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")

        except Exception as e:
            return {"error": "timestamp not following format %Y-%m-%dT%H:%M:%S"}, 400

        query.update({"timestamp": {"$gte": start, "$lte": end}})

    data = list(db.sound.aggregate([
        {
            '$match': query
        }, {
            '$group': {
                '_id': '$sensorId',
                'soundCount': {
                     '$count': {}
                },
                'sound': {
                    '$push': {
                        'timestamp': '$timestamp',
                        'sound': '$sound'
                    }
                }
            }
        }
    ]))

    if data:
        data = data[0]
        if "_id" in data:
            del data["_id"]
            data.update({"sensorId": sensorId})

        for sound in data['sound']:
            sound["timestamp"] = sound["timestamp"].strftime("%Y-%m-%dT%H:%M:%S")

        return data
    else:
        return {"error": "id not found"}, 404

app.run()
