from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# client = MongoClient("localhost:27017") --> this also works
try:
 client = MongoClient(port=27017)
except Exception as inst:
 print("Unexpected error in 8 :", "8: "+inst)
# Set the db object to point to the myapp database
db=client.myapp
# Showcasing the count() method of find, count the total number of 5 ratings 
print('The number of products available:')
# fivestarcount = db.reviews.find({'rating': 5}).count()
#productsCount = db.products.find().count();
#print(productsCount)

def productCount():
 try:
  productsCount = db.products.find().count()
  return str(productsCount);
 except Exception as inst:
  print("Unexpected error in 23:", "23: "+inst)
  return str(inst);
 