from generator import *
from time import gmtime, strftime

class Jon(Generator):
  
  def getNoun(self):
    return "clock that reads " + strftime("%H:%M:%S", gmtime())

  def getAdjective(self):
    return "cheerful"

  def getTemplate(self):
    return "I think a {{adjective}} {{noun}} is better than {{gcse}}"