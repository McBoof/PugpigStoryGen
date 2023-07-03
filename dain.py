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