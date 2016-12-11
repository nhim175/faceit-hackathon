import pymongo
from pymongo import MongoClient
import pprint
person_id = 1
import time

client = MongoClient('mongodb://47.91.16.198:27017')
db = client.faceit
# Get the userId for the classifyID
db_id = db['UserClassifyId']
record = db_id.find_one({"classifyId": person_id})
user_id = record['userId']

# Content to push
event_id = "pHJ9fGNMxNMh88pGH"
type = "in"
created_at = time.time()
post = {"userId": user_id,
        "eventId": event_id,
        "type": type,
        "createdAt": created_at}

db_to_push = db['CheckInOutQueue']
post_id = db_to_push.insert_one(post).inserted_id
print(post_id)
#db_to_push.collection_names(include_system_collections=False)[u'posts']