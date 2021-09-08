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

# new_docs = [{
#     "first": "john",
#     "last": "lennon",
#     "dob": "09/10/1940",
#     "gender": "m",
#     "hair_color": "brown",
#     "occupation": "beatle",
#     "nationality": "british"
# }, {
#     "first": "eve",
#     "last": "ryan",
#     "dob": "19/09/1992",
#     "gender": "f",
#     "hair_color": "pink",
#     "occupation": "developer",
#     "nationality": "irish"
# }, {
#     "first": "martha",
#     "last": "fenton",
#     "dob": "15/05/1974",
#     "gender": "f",
#     "hair_color": "brown",
#     "occupation": "manager",
#     "nationality": "irish"
# }, {
#     "first": "neil",
#     "last": "hanslem",
#     "dob": "14/07/1983",
#     "gender": "m",
#     "hair_color": "blonde",
#     "occupation": "actor",
#     "nationality": "british"
# }, {
#     "first": "rocky",
#     "last": "persolm",
#     "dob": "19/12/1994",
#     "gender": "f",
#     "hair_color": "black",
#     "occupation": "activist",
#     "nationality": "american"
# }]

# coll.insert_many(new_docs)

print("Reading collection...")

documents = coll.find()


for doc in documents:
    print(doc)


print("...collection read!")
