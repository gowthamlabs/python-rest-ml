from flask import Flask, jsonify, Response
from pymongo import MongoClient
from app.util.MongoConnector import *
from app.model.ErrorMessage import *
import pickle
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
  errObj = ErrorMessage();
  #errObj.set_message(str(inst));
  #print(errObj.get_message());
  errObj.err_message = str(inst);
  emList = [];
  emList.append(errObj)
  my_pickled_mary = pickle.dumps(emList)
  return Response(my_pickled_mary);

 
if __name__ == '__main__':
 app.run()
	# for enabling debug mode app.run(debug=True)