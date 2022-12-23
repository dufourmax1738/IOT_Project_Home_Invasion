import pymongo
import requests
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from flask_objectid_converter import ObjectIDConverter
from pymongo.server_api import ServerApi
import datetime as dt


from DevicesApi import get_All_Devices_For_Home, get_Device_From_Device_Name

from SensorSchemas import SoundSensorSchema, MotionSensorSchema

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


def getTimeStamp():
    return dt.datetime.today().replace(microsecond=0)

sensors = Blueprint('sensors', __name__, template_folder='templates')





@sensors.route("/sensors/<int:sensorId>/sound", methods=["POST"])
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


@sensors.route("/sensors/<int:sensorId>/motion", methods=["POST"])
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


@sensors.route("/sensors/<int:sensorId>/motion")
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

    query.update({"motion" : 1})
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
            motion["timestamp"] = motion["timestamp"].strftime("%Y-%m-%dT%H:%M:%S")

        return data
    else:
        return {"error": "id not found"}, 404





@sensors.route("/sensors/<int:sensorId>/sound")
def get_sensor_sound(sensorId):
    # em.postSound()
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

@sensors.route("/homes/<string:home>/devices/<string:device>/average")
def get_sound_average_for_home(home, device):
    homeDevices = get_All_Devices_For_Home(home)[0]
    soundSensors = []
    for device in homeDevices[0]["devices"]:
        soundSensors.append(device["soundSensorId"])
    sound = []

    query = {"sensorId": { "$in" : soundSensors }}

    start = request.args.get("start")
    end = request.args.get("end")

    data = list(db.sound.aggregate([
        {
            '$match': query
        }, {
            '$group': {
                '_id': '$sensorId',
                'soundAvg': {
                    '$avg': '$sound'
                }
            }
        }
    ]))
#http://127.0.0.1:5000/homes/testHome/devices/testDevice/average?start=2021-12-05T14:01:29&end=2023-12-22T19:18:00   <-- POSTMAN URL Example

    return data


@sensors.route("/homes/<string:home>/motion")
def get_Motion_Count_For_Home(home):
    homeDevices = get_All_Devices_For_Home(home)[0]
    motionSensors = []
    for device in homeDevices[0]["devices"]:
        motionSensors.append(device["motionSensorId"])
    motion = []

    start = request.args.get("start")
    end = request.args.get("end")

    for sensor in motionSensors:
        motion.append(requests.get("http://127.0.0.1:5000/sensors/"+str(sensor)+"/motion?start="+str(start)+"&end="+str(end)).json())


    return motion


@sensors.route("/homes/<string:home>/devices/<string:device>/motion")
def  get_Motion_Count_For_Device(home,device):
    homeDevice = get_Device_From_Device_Name(home, device)[0]

    start = request.args.get("start")
    end = request.args.get("end")

    return requests.get("http://127.0.0.1:5000/sensors/"+str(homeDevice[0]["devices"]["motionSensorId"])+"/motion?start="+str(start)+"&end="+str(end)).json()

