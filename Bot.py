from flask import Flask, jsonify
from pymongo import MongoClient
from app.util.MongoConnector import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
 try:
  db = MongoConnector.db_connect();
  productsCount = db.products.find().count();
  print(str(productsCount));
  MongoConnector.db_close();
  return str(productsCount);
 except Exception as inst:
  return str(inst);

 
if __name__ == '__main__':
 app.run()
	# for enabling debug mode app.run(debug=True)