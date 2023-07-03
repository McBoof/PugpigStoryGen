
class Generator:
  
  def __init__(self, color):
    self.color = color

  def getColor(self):
    return self.color

  def getGcse(self):
    return "Computer Science"

  def getTemplate(self):
    return """
One day the {{noun}} went to see the {{noun}} at the park, and talked about {{noun}}s. They also bought a {{adjective}} {{adjective}} {{noun}} and a {{adjective}} {{noun}} from the {{noun}}, but that wasn't until after they ate the {{adjective}} {{noun}}. There was a {{gcse}} the next day.
"""
  
  def getWord(self, type):
    methodName = "get" + type.capitalize()
    if (hasattr(self, methodName)):
      return getattr(self, methodName)()  
    else:
      return "???"+methodName