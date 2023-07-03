from generator import *
import random
choiceAdj = ["stronk","powerful","soprendente","triste","felicdad","Brave", "resilient", "determined","Passionate", "creative", "innovative","Kind", "compassionate", "empathetic","Adventurous", "spontaneous", "fearless", "Intelligent", "knowledgeable", "insightful", "Honest", "trustworthy", "reliable", "Generous", "selfless", "charitable", "Ambitious", "driven", "focused","Loyal", "supportive", "dependable","Talented", "skillful", "versatile"]
choiceNou = ["rat", "pigeon", "monkey", "swordfish", "dain", "Mountain", "river", "forest", "Car", "bike", "scooter", "Book", "magazine", "newspaper", "Dog", "cat", "bird", "Table", "chair", "lamp", "House", "apartment", "cottage", "Pen", "pencil", "marker", "Phone", "tablet", "laptop", "Pizza", "burger", "sandwich", "Tree", "flower", "bush"]
class Minh(Generator):

  
  def getNoun(self):
    noun = random.choice(choiceNou)
    return noun
  def getAdjective(self):
    adjective = random.choice(choiceAdj)
    return adjective
  