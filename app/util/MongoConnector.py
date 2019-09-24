from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

class MongoConnector:
 db_name = "myapp"
 
 #def __init__(self):
  
 
 def db_connect():
  # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
  # client = MongoClient("localhost:27017") --> this also works
  client = MongoClient(port=27017)
  # Set the db object to point to the myapp database
  db = client.myapp
  try: 
   db.command("serverStatus")
   return db
  except Exception as e:
   raise Exception("No connection could be made because the target machine actively refused it");

 def db_close():
  client.close();
    
   
  # fivestarcount = db.reviews.find({'rating': 5}).count()
  #productsCount = db.products.find().count();
  #print(productsCount)