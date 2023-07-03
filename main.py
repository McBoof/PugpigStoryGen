import random
import colorama
from colorama import Back

from generator import *
from jon import *
from noah import *
from Lisbeth import *

g = Noah(Back.BLUE)
g = Lisbeth(Back.RED)

generators = [
  Jon(Back.BLUE),
  Noah(Back.GREEN), Lisbeth(Back.RED)
]

template = """
One day the {{adjective}} went to the {{noun}} and saw the {{adjective}} {{noun}}".
They also bought a {{adjective}} {{adjective}} {{noun}} and a {{adjective}} {{noun}}.
"""

replacements = ["adjective", "noun"]

for word_type in replacements:
  
  placeholder = "{{"+word_type+"}}"  
  print(placeholder)
  while template.find(placeholder) > 0:
    g = random.choice(generators)
    template = template.replace(placeholder, g.getColor() + g.getWord(word_type) + Back.BLACK, 1)  

  

print(template)
