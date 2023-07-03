from generator import *
import random
choiceadj = ["Delectable","Crispy","Dead","Yummy"]
choicenou = ["Komodo Dragon","Human Flesh","Bomb"]
class Dain(Generator):



  def getNoun(self):
    noun = random.choice(choicenou)
    return noun

  def getAdjective(self):
    adjective = random.choice(choiceadj)
    return adjective 

  def getTemplate(self):
    return "The {{noun}} ate the {{adjective}} {{noun}}, but not before roasting the {{adjective}} {{noun}} alive, and feasting on their screams. Then they ran over to the {{adjective}} toilet, and took a {{adjective}} dump."