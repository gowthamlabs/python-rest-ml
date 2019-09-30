from ..dao.BotDAO import *

class BotHelper:

 def get_profitMsg(prodCount):
  try:
   if(int(prodCount) >= 15):
    messageSummary = "Profit is high";
   print("Returned from BotHelper");
   return messageSummary;
  
  except Exception as inst:
   return str(inst);