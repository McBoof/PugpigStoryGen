
class Generator:
  
  def __init__(self, color):
    self.color = color

  def getColor(self):
    return self.color


  def getNoun(self):
    return "boo"
  
  def getAdjective(self):
    return "green"
  
  def getWord(self, type):
    methodName = "get" + type.capitalize()
    if (hasattr(self, methodName)):
      return getattr(self, methodName)()  
    else:
      return "???"+methodName