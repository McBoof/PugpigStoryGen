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

g = random.choice(generators)
template = g.getTemplate()

replacements = ["adjective", "noun", "gcse"]

for word_type in replacements:
  
  placeholder = "{{"+word_type+"}}"
  while template.find(placeholder) > 0:
    g = random.choice(generators)
    template = template.replace(placeholder, g.getColor() + g.getWord(word_type) + Back.BLACK, 1)  

  

print(template)
