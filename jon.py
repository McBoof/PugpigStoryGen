from generator import *
class Jon(Generator):
  
  def getNoun(self):
    return "dog"

  def getAdjective(self):
    return "cheerful"

  def getTempate(self):
    return "{{adjective}} {{noun}}"