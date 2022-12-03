import pymongo as pymongo
from pymongo import ReturnDocument
from flask import Flask, request, jsonify, Blueprint
import DevicesApi

client = pymongo.MongoClient("mongodb+srv://MaxDufour:5uwLOgDI1k8Qf1Op@iotfinalproject.ldavcfn.mongodb.net/?retryWrites=true&w=majority")
db = client.HomeInvasions

devices = Blueprint('devices', __name__, template_folder='templates')

@devices.route('/homes/<home>/devices',methods=["GET"])
def get_All_Devices_For_Home():
    # cursor = db.homes.find({},{"name":1,"_id":0})
    # homes = list(cursor)

    return jsonify({"ping":"pong"}), 200

@devices.route('/homes/<home>/devices',methods=["POST"])
def add_Device_For_Home(home):
    # if error:
    #     return error, 400
    query = {"name": home}
    newValue = {"$push": {"devices": request.json}}
    updatedHome = db.homes.find_one_and_update(query, newValue, {"name": 1, "_id": 0, "devices":1},
                                               return_document=ReturnDocument.AFTER, upsert=False, )

    return jsonify(updatedHome), 200
