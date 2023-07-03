import random
import colorama
from colorama import Back

from generator import *
from jon import *
from noah import *
from lisbeth import *
from nasreen import *
from minh import *
from abdulah import *
from nathan import *
from dain import *

g = Noah(Back.BLUE)
generators = [
  Jon(Back.BLUE),
  Noah(Back.GREEN),
  Minh(Back.YELLOW),
  Abdulah(Back.RED),
  Nathan(Back.MAGENTA),
  Dain(Back.LIGHTMAGENTA_EX),
  Lisbeth(Back.LIGHTWHITE_EX),
  Nasreen(Back.CYAN)
]

template = """
One day the {{noun}} went to see the {{noun}} at the park, and talked about {{noun}}s. They also bought a {{adjective}} {{adjective}} {{noun}} and a {{adjective}} {{noun}} from the {{noun}}, but that wasn't until after they ate the {{adjective}} {{noun}}. There was a {{gcse}} the next day.
"""

replacements = ["adjective", "noun", "gcse"]

for word_type in replacements:
  
  placeholder = "{{"+word_type+"}}"
  while template.find(placeholder) > 0:
    g = random.choice(generators)
    template = template.replace(placeholder, g.getColor() + g.getWord(word_type) + Back.BLACK, 1)  

  

print(template)
