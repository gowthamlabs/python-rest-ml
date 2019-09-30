from ..util.MongoConnector import *

class BotDAO:

 def get_productsCount():
  try:
   db = MongoConnector.db_connect();
   productsCount = db.products.find().count();
   print(str(productsCount));
   #MongoConnector.db_close();
   return productsCount;
  
  except Exception as inst:
   #MongoConnector.db_close();
   return str(inst);