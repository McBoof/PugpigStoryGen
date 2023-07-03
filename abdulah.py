from generator import *
import random

class Abdulah(Generator):
  
  def getNoun(self):
    nouns = ["Chair", "Laptop", "Sun", "Moon", "Ocean", "Mountain", "Cloud", "Car", "Bicycle", "Bird", "Tree", "Book", "Table", "Phone", "Camera", "Dog", "Cat", "House", "City", "Garden", "Bridge", "River", "Lake", "Flower", "Star", "Island", "Beach", "Sword", "Shield", "Key", "Door", "Window", "Music", "Painting", "Movie", "Light", "Fire", "Earth", "Air", "Water", "Tiger", "Elephant", "Monkey", "Dolphin", "Whale"]
    noun = random.choice(nouns)
    return noun

  def getAdjective(self):
    adjectives = ["Beautiful", "Vibrant", "Serene", "Majestic", "Glowing", "Graceful", "Fluffy", "Cozy", "Loyal", "Playful", "Intriguing", "Sturdy", "Smart", "High-resolution", "Fast", "Sleek", "Tall", "Bustling", "Enchanting", "Mighty", "Melodious", "Vibrant", "Captivating", "Soft", "Warm", "Fertile", "Refreshing", "Crystal-clear", "Striped", "Gentle", "Curious"]
    adjective = random.choice(adjectives)
    return adjective

  def getGcse(self):
    gcses = ["Mathematics", "English Language", "English Literature", "Science (Physics, Chemistry, Biology)", "History", "Geography", "Modern Foreign Languages (French, German, Spanish, etc.)", "Art and Design", "Music", "Physical Education (PE)", "Computer Science", "Business Studies", "Religious Studies", "Design and Technology", "Drama", "Sociology", "Psychology", "Economics", "Health and Social Care", "Media Studies"]
    gcse = random.choice(gcses)
    return gcse

  def Template(self):
    return """
    Once upon a time, in a {{adjective}} town, lived a {{gcse}} student named {{noun}}. {{noun}} was known for {{adjective}} dedication and {{adjective}} passion for {{verb}}.

In the morning, {{noun}} would {{verb}} up early to {{verb}} for a day filled with {{gcse}} subjects. Armed with {{adjective}} textbooks and {{adjective}} stationery, {{noun}} would {{verb}} on {{adjective}} journeys through the realms of Mathematics, English Language, and Science.

During Mathematics class, {{noun}} would {{verb}} {{adjective}} equations and {{verb}} complex problems with a {{noun}} in hand. {{noun}}'s logical mind and {{adjective}} problem-solving skills made {{noun}} a standout student in the classroom.

In English Language lessons, {{noun}} would {{verb}} the beauty of words and {{verb}} into {{adjective}} literary works. {{noun}}'s {{adjective}} imagination would {{verb}} as {{noun}} {{verb}} {{adjective}} stories and {{verb}} powerful pieces of writing.

In the Science laboratory, {{noun}} would {{verb}} experiments and {{verb}} {{adjective}} phenomena. With {{adjective}} safety goggles and {{adjective}} curiosity, {{noun}} would {{verb}} the secrets of the universe, from the laws of physics to the wonders of chemistry and biology.

During breaks, {{noun}} would {{verb}} {{adjective}} discussions on History, Geography, and {{gcse}} subjects. {{Verb}} in debates, {{noun}} would {{verb}} {{adjective}} knowledge and {{verb}} in intellectual conversations with {{adjective}} classmates.

As the school day {{verb}} to an end, {{noun}} would {{verb}} in {{adjective}} extracurricular activities, such as {{gcse}} club meetings, {{adjective}} sports practices, and {{adjective}} music rehearsals. {{noun}}'s {{adjective}} talents {{verb}} beyond academics, making {{noun}} a well-rounded individual.

In the evenings, {{noun}} would {{verb}} to {{noun}}'s {{adjective}} study corner, surrounded by {{adjective}} textbooks and revision guides. With {{adjective}} determination, {{noun}} would {{verb}} for upcoming {{gcse}} exams, {{verb}} reviewing the intricate details of each subject.

Throughout the {{verb}} of being a {{gcse}} student, {{noun}} {{verb}} {{adjective}} challenges and {{verb}} moments of self-doubt. However, {{noun}} {{verb}} with {{adjective}} resilience and sought help from {{adjective}} teachers and {{adjective}} classmates, who {{verb}} guidance and support.

The day of the {{gcse}} results {{verb}}, filled with {{adjective}} anticipation. With {{verb}} hands, {{noun}} {{verb}} the envelope and discovered {{adjective}} accomplishments. The hard work and dedication had {{verb}} off, as {{noun}} {{verb}} {{adjective}} grades in all {{gcse}} subjects.

With a sense of fulfillment and {{adjective}} excitement, {{noun}} {{verb}} ahead to the future, where {{noun}} would {{verb}} {{gcse}} subjects at a higher level and {{verb}} new {{noun}} and challenges.

And so, the story of the {{gcse}} student named {{noun}} {{verbs}} as a reminder of the transformative power of education, resilience, and the pursuit of knowledge.
"""