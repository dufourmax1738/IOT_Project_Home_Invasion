import pymongo as pymongo
from pymongo import ReturnDocument
from flask import Flask, request, jsonify
from HomeSchema import HomeSchema
from DevicesApi import devices

homes = Flask(__name__)
homes.register_blueprint(devices)
homes.config['DEBUG'] = True

client = pymongo.MongoClient("mongodb+srv://MaxDufour:5uwLOgDI1k8Qf1Op@iotfinalproject.ldavcfn.mongodb.net/?retryWrites=true&w=majority")
db = client.HomeInvasions


@homes.route('/homes/<home>', methods=["DELETE"])
def delete_Home(home):

    if(db.homes.delete_many({"name":home}).deleted_count):
        return jsonify({"deleted_home": home}), 200
    return jsonify({"error": "No such home"}), 400


@homes.route('/homes', methods=["POST"])
def add_Home():
    error = HomeSchema().validate(request.json)
    if error:
        return error, 400

    if(len(list(db.homes.find({"name":request.json["name"]})))):
        return jsonify({"error": "name already exists"}), 400

    db.homes.insert_one(request.json)

    return jsonify({"name" : request.json["name"]})
@homes.route('/homes', methods=["GET"])
def get_All_Homes():
    cursor = db.homes.find({},{"name":1,"_id":0,"devices":1})
    homes = list(cursor)

    return jsonify(homes), 200
@homes.route('/homes/<home>', methods=["GET"])
def get_Home_By_Name(home):
    cursor = db.homes.find({"name":home},{"name":1,"_id":0,"devices":1})
    homes = list(cursor)

    return jsonify(homes), 200

@homes.route('/homes/<home>', methods=["PUT"])
def update_Home_Name(home):
    error = HomeSchema().validate(request.json)
    if error:
        return error, 400

    if (len(list(db.homes.find({"name": request.json["name"]})))):
        return jsonify({"error": "name already exists"}), 400

    query = {"name":home}
    newValue = {"$set":{"name":request.json["name"]}}
    updatedHome = db.homes.find_one_and_update(query,newValue,{"name":1,"_id":0},return_document=ReturnDocument.AFTER, upsert=False,)

    return jsonify(updatedHome), 200






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    homes.run()



