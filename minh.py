from generator import *
import random
choiceAdj = ["stronk","powerful","soprendente","triste","felicdad"]
choiceNou = ["rat","pigeon","monkey","swordfish","dain"]
class Minh(Generator):

  
  def getNoun(self):
    noun = random.choice(choiceNou)
    return noun
  def getAdjective(self):
    adjective = random.choice(choiceAdj)
    return adjective
  