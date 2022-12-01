import pymongo as pymongo
from flask import Flask, request, jsonify
from HomeSchema import HomeSchemaPost

app = Flask(__name__)
app.config['DEBUG'] = True

client = pymongo.MongoClient("mongodb+srv://MaxDufour:5uwLOgDI1k8Qf1Op@iotfinalproject.ldavcfn.mongodb.net/?retryWrites=true&w=majority")
db = client.HomeInvasions


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

    return jsonify(homes)
@app.route('/homes/<home>',methods=["GET"])
def get_Home_By_Name(home):
    cursor = db.homes.find({"name":home},{"name":1,"_id":0})
    homes = list(cursor)

    return jsonify(homes)




    #return db.homes.insert_one({"name":"Dufour's Home"}).inserted_id



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()



