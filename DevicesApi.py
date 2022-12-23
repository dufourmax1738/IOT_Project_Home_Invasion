import pymongo as pymongo
from pymongo import ReturnDocument
from flask import Flask, request, jsonify, Blueprint
from DeviceSchema import DeviceSchema

client = pymongo.MongoClient("mongodb+srv://MaxDufour:5uwLOgDI1k8Qf1Op@iotfinalproject.ldavcfn.mongodb.net/?retryWrites=true&w=majority")
db = client.HomeInvasions

devices = Blueprint('devices', __name__, template_folder='templates')

@devices.route('/homes/<home>/devices',methods=["GET"])
def get_All_Devices_For_Home(home):
    cursor = db.homes.aggregate([
    {
        '$match': {
            'name': home
        }
    }, {
        '$project': {
            '_id': 0,
            'name': 1,
            'devices': 1
        }
    }, {
        '$project': {
            'name': 0
        }
    }])
    homes = list(cursor)

    return jsonify(homes), 200

@devices.route('/homes/<home>/devices/<device>', methods=["GET"])
def get_Device_From_Device_Name(home, device):
    cursor = db.homes.aggregate([
    {
        '$match': {
            'name': home
        }
    }, {
        '$unwind': {
            'path': '$devices'
        }
    }, {
        '$match': {
            'devices.name': device
        }
    }, {
        '$project': {
            '_id': 0,
            'name': 0
        }
    }
    ])
    homes = list(cursor)

    return homes, 200

@devices.route('/homes/<home>/devices',methods=["POST"])
def add_Device_For_Home(home):
    error = DeviceSchema().validate(request.json)
    if error:
        return error, 400

    if (len(list(db.homes.find({"name": home,"devices.name":request.json["name"]})))):
        return jsonify({"error": "name already exists"}), 400

    query = {"name": home}
    newValue = {"$push": {"devices": request.json}}
    updatedHome = db.homes.find_one_and_update(query, newValue, {"name": 1, "_id": 0, "devices": 1},
                                               return_document=ReturnDocument.AFTER, upsert=False)

    return jsonify(updatedHome), 200

@devices.route('/homes/<home>/devices/<device>',methods=["DELETE"])
def delete_Device_For_Home(home, device):
    query = {"name": home}
    newValue = {"$pull": {"devices": {"name":device}}}
    updatedHome = db.homes.find_one_and_update(query, newValue, {"name": 1, "_id": 0, "devices": 1},
                                               return_document=ReturnDocument.AFTER, upsert=False)

    return jsonify(updatedHome), 200

@devices.route('/homes/<home>/devices/<device>',methods=["PUT"])
def update_Device_For_Home(home, device):

    error = DeviceSchema().validate(request.json)
    if error:
        return error, 400
    query = {"name": home}

    if (len(list(db.homes.find({"name": home,"devices.name":request.json["name"]})))):
        return jsonify({"error": "name already exists"}), 400

    newValue = {"$pull": {"devices": {"name": device}}}
    db.homes.find_one_and_update(query, newValue)

    newValue = {"$push": {"devices": request.json}}
    updatedHome = db.homes.find_one_and_update(query, newValue, {"name": 1, "_id": 0, "devices": 1},
                                               return_document=ReturnDocument.AFTER, upsert=False)

    return jsonify(updatedHome), 200