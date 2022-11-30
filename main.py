import pymongo as pymongo
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

client = pymongo.MongoClient("mongodb+srv://MaxDufour:5uwLOgDI1k8Qf1Op@iotfinalproject.ldavcfn.mongodb.net/?retryWrites=true&w=majority")
db = client.HomeInvasions

def print_hi():
    cursor = db.homes.find()
    homes = list(cursor)
    for home in homes:
        if "_id" in home:
            home["_id"] = str(home["_id"])

    return jsonify(homes)
    #return db.homes.insert_one({"name":"Dufour's Home"}).inserted_id



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

app.run()

