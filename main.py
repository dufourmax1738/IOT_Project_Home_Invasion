import pymongo as pymongo

import emulator as em
from flask import Flask, request, jsonify
from flask_objectid_converter import ObjectIDConverter
from pymongo import ReturnDocument
from pymongo.server_api import ServerApi

from HomesApi import homes
from SensorApi import sensors
from SensorSchemas import SoundSensorSchema, MotionSensorSchema
from bson import json_util, ObjectId
from flask_cors import CORS
import datetime as dt

# loading private connection information from environment variables
from dotenv import load_dotenv

from pymongo import ReturnDocument
from flask import Flask, request, jsonify
from HomeSchema import HomeSchema
from DevicesApi import devices

app = Flask(__name__)
app.register_blueprint(devices)
app.register_blueprint(homes)
app.register_blueprint(sensors)
app.config['DEBUG'] = True
app.url_map.converters['objectid'] = ObjectIDConverter

CORS(app)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()



