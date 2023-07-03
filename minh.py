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
  def getTempate(self):
    return "Once upon a time, in a {{noun}} far away, there lived a {{adjective}} {{noun}}. This {{noun}} was known for its {{adjective}} and {{adjective}} nature. One day, the {{noun}} embarked on a journey to explore the nearby {{noun}}. As the {{noun}} wandered through the dense {{noun}}, it encountered a {{adjective}} {{noun}}. The {{noun}} and the {{noun}} exchanged {{adjective}} glances, instantly forming a bond. Together, they continued their adventure, venturing deeper into the heart of the {{noun}}. During their exploration, the {{noun}} and the {{noun}} stumbled upon a hidden treasure , a magnificent {{noun}} made of {{adjective}} {{noun}}. It shimmered under the sunlight, captivating their eyes. Excitedly, they decided to share the discovery with the villagers. News of the enchanting {{noun}} spread rapidly throughout the land. People from far and wide flocked to witness its {{adjective}} beauty. The {{noun}} and the {{noun}} became local heroes, celebrated for their bravery and curiosity. In time, the {{noun}} and the {{noun}} realized that their journey together had transformed not only their own lives but also the lives of those around them. The {{adjective}} spirit of adventure and the bond they shared inspired others to embrace the unknown and appreciate the {{adjective}} wonders of the world. And so, the story of the {{adjective}} {{noun}} and the {{adjective}} {{noun}} became a legend, passed down from generation to generation, reminding everyone of the power of curiosity, friendship, and the magic that lies within the heart of every {{noun}}."