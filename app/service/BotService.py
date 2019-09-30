from ..dao.BotDAO import *
from ..helper.BotHelper import *

class BotService:

 def get_productsCount():
  try:
   messageSummary = BotHelper.get_profitMsg(BotDAO.get_productsCount());
   print("Returned from BotService");
   return messageSummary;
  
  except Exception as inst:
   return str(inst);