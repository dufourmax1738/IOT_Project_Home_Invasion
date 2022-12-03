import pymongo as pymongo
from pymongo import ReturnDocument
from flask import Flask, request, jsonify
from HomeSchema import HomeSchemaPost

app = Flask(__name__)
app.config['DEBUG'] = True

client = pymongo.MongoClient("mongodb+srv://MaxDufour:5uwLOgDI1k8Qf1Op@iotfinalproject.ldavcfn.mongodb.net/?retryWrites=true&w=majority")
db = client.HomeInvasions


@app.route('/homes/<home>', methods=["DELETE"])
def delete_Home(home):

    if(db.homes.delete_many({"name":home}).deleted_count):
        return jsonify({"deleted_home": home}), 200
    return jsonify({"error": "No such home"}), 400


@app.route('/homes',methods=["POST"])
def add_Home():
    error = HomeSchemaPost().validate(request.json)
    if error:
        return error, 400

    db.homes.insert_one(request.json)

    return jsonify({"name" : request.json["name"]})
@app.route('/homes',methods=["GET"])
def get_All_Homes():
    cursor = db.homes.find({},{"name":1,"_id":0})
    homes = list(cursor)

    return jsonify(homes), 200
@app.route('/homes/<home>',methods=["GET"])
def get_Home_By_Name(home):
    cursor = db.homes.find({"name":home},{"name":1,"_id":0})
    homes = list(cursor)

    return jsonify(homes), 200

@app.route('/homes/<home>', methods=["PUT"])
def update_Home_Name(home):
    error = HomeSchemaPost().validate(request.json)
    if error:
        return error, 400
    query = {"name":home}
    newValue = {"$set":{"name":request.json["name"]}}
    argument = {"returnOriginal": "false"}
    updatedHome = db.homes.find_one_and_update(query,newValue,{"name":1,"_id":0},return_document=ReturnDocument.AFTER, upsert=False,)

    return jsonify(updatedHome), 200






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()



