from generator import *
import random
class Noah(Generator):
  nouns = [
  ["ladybird", "butterfly", "bird", "beetle", "squid"],
  ["brick", "tree", "phone"],
  ["London", "New York", "Melbourne", "Tokyo"]
  ]

  adjectives = [
  ["cool", "slick", "awesome"],
  ["slimy", "wet", "miniscule", "elephantine", "invisible", "bouncy"],
  ["broken", "ugly"]
  ]
  
  def getNoun(self):
    type = Noah.nouns[random.randint(0, len(Noah.nouns)-1)]
    noun = type[random.randint(0, len(type)-1)]
    return noun

  def getAdjective(self):
    type = Noah.adjectives[random.randint(0, len(Noah.adjectives)-1)]
    adjective = type[random.randint(0, len(type)-1)]
    return adjective

