import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo connected")
        return conn
    except pymongo.errors.ConnectionFailure as err:
        print("Could not connect to MongoDB: %s") % err


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# new_doc = {
#            "first": "douglas",
#            "last": "adams",
#            "dob": "11/03/1952",
#            "hair_color": "grey",
#            "occupation": "writer",
#            "nationality": "british"
# }

new_docs = [{
    "first": "terry",
    "last": "pratchett",
    "dob": "28/04/1948",
    "gender": "m",
    "hair_color": "not much",
    "occupation": "writer",
    "nationality": "british"
}, {
    "first": "george",
    "last": "rr martin",
    "dob": "20/09/1948",
    "gender": "m",
    "hair_color": "white",
    "occupation": "writer",
    "nationality": "american"
}]

# coll.insert_many(new_docs)

print("Reading collection...")

documents = coll.find()


for doc in documents:
    print(doc)


print("...collection read!")
