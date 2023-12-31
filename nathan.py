from generator import *
import random
class Nathan(Generator):
  nounslist = [
    "Table",
    "Chair",
    "Dog",
    "Cat",
    "Car",
    "Book",
    "Tree",
    "House",
    "Ball",
    "Phone",
    "Computer",
    "Flower",
    "River",
    "Mountain",
    "Sun",
    "Moon",
    "Star",
    "Cloud",
    "Bird",
    "Fish",
    "Elephant",
    "Lion",
    "Tiger",
    "Butterfly",
    "Turtle",
    "Pizza",
    "Guitar",
    "Drum",
    "Keyboard",
    "Microphone",
    "Telescope",
    "Camera",
    "Radio",
    "Bike",
    "Boat",
    "Plane",
    "Train",
    "Ship",
    "Wallet",
    "Backpack",
    "Key",
    "Knife",
    "Spoon",
    "Fork",
    "Plate",
    "Glass",
    "Cup",
    "Hat",
    "Shoe",
    "Bag",
    "Watch",
    "Clock",
    "Mirror",
    "Lamp",
    "Candle",
    "Pen",
    "Pencil",
    "Paper",
    "Bookshelf",
    "Camera",
    "Photo",
    "Ring",
    "Necklace",
    "Bracelet",
    "Earrings",
    "Guitar",
    "Violin",
    "Drum",
    "Paintbrush",
    "Sculpture",
    "Statue",
    "Toy",
    "Doll",
    "Teddy bear",
    "Puzzle",
    "Board game",
    "Robot",
    "Globe",
    "Map",
    "Telescope",
    "Microscope",
    "Feather",
    "Shell",
    "Rock",
    "Sand",
    "Seashell",
    "Coral",
    "Leaf",
    "Branch",
    "Acorn",
    "Pinecone",
    "Pineapple",
    "Banana",
    "Apple",
    "Orange",
    "Grape",
    "Watermelon",
    "Tomato",
    "Cucumber",
    "Carrot",
    "Zigglywomp",
    "Land",
    "Flibberdoodle",
    "Creature",
    "Quibblesnatch",
    "Zonkedoodle",
    "Mane",
    "Wings",
    "Eyes",
    "Disco balls",
    "Gloobertide",
    "Quest",
    "Bananaflibber",
    "Legends",
    "Object",
    "Gigglesnort",
    "Rubber duck",
    "Pair",
    "Mismatched socks",
    "Forest",
    "Trees",
    "Secrets",
    "Mushrooms",
    "Swarm",
    "Flibberfrogs",
    "Harmony",
    "Orchestra",
    "Rubber duck",
    "Virtuoso",
    "Cacophony",
    "Mayhem",
    "Wibblywocky",
    "Snickersnort",
    "Tutu",
    "Top hat",
    "Cheese",
    "Tea party",
    "Troupe",
    "Tap-dancing teapots",
    "Waltzing walruses",
    "Wonderland",
    "Kaleidoscope",
    "Characters",
    "Snufflymuffin",
    "Opera",
    "Bananas",
    "Bumbling wumblebee",
    "Propeller",
    "Bum",
    "Dandyflop",
    "Monocle",
    "Cheese curds",
    "Laughter",
    "Chaos",
    "Bananaflibber",
    "Disco ball",
    "Confetti",
    "Marshmallow clouds",
    "Giggles",
    "Madness",
    "Jig",
    "Crew",
    "Air",
    "Melodies",
    "Squishy cheese curds",
    "Quest",
    "Celebration",
    "Zonkedoodle",
    "Pocketful",
    "Laughter",
    "Heart",
    "Whimsy",
    "Jester",
    "Flabbergast",
    "Blunderbuss",
    "Gobbledygook",
    "Shimmer",
    "Noodle",
    "Whippersnapper",
    "Fantasmagoria",
    "Hodgepodge",
    "Pandemonium",
    "Sassafras",
    "Wobblewop",
    "Brouhaha",
    "Hootenanny",
    "Gadzooks",
    "Wunderkind",
    "Nonsense",
    "Quizzity"
  ]

  adjectiveslist = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Small",
    "Big",
    "Happy",
    "Sad",
    "Angry",
    "Funny",
    "Serious",
    "Tall",
    "Short",
    "Fast",
    "Slow",
    "Beautiful",
    "Ugly",
    "Old",
    "Young",
    "Thin",
    "Thick",
    "Soft",
    "Hard",
    "Bright",
    "Dark",
    "Brave",
    "Cowardly",
    "Smart",
    "Stupid",
    "Clever",
    "Clumsy",
    "Kind",
    "Mean",
    "Polite",
    "Rude",
    "Friendly",
    "Hostile",
    "Gentle",
    "Harsh",
    "Calm",
    "Anxious",
    "Honest",
    "Dishonest",
    "Generous",
    "Stingy",
    "Patient",
    "Impatient",
    "Courageous",
    "Fearful",
    "Loud",
    "Quiet",
    "Energetic",
    "Lazy",
    "Silly",
    "Graceful",
    "Awkward",
    "Sincere",
    "Fake",
    "Modest",
    "Arrogant",
    "Creative",
    "Dull",
    "Adventurous",
    "Cautious",
    "Fierce",
    "Gentle",
    "Curious",
    "Indifferent",
    "Shy",
    "Confident",
    "Insecure",
    "Wise",
    "Foolish",
    "Careful",
    "Careless",
    "Cheerful",
    "Gloomy",
    "Unique",
    "Ordinary",
    "Delicious",
    "Disgusting",
    "Sunny",
    "Rainy",
    "Wind",
    "Breezy",
    "Cold",
    "Hot",
    "Fresh",
    "Stale",
    "Noisy",
    "Peaceful",
    "Busy",
    "Empty",
    "Wild",
    "Calm",
    "Clean",
    "Dirty",
    "Busy",
    "Free",
    "Peculiar",
    "Floofy",
    "Purple",
    "Polka-dotted",
    "Googly",
    "Sunny",
    "Mystic",
    "Whimsical",
    "Melodious",
    "Zonked",
    "Mismatched",
    "Lively",
    "Perfect",
    "Amphibious",
    "Whimsical",
    "Quirky",
    "Flaming",
    "Bumbling",
    "Dandy",
    "Nonsensical",
    "Jubilant",
    "Utterly absurd",
    "Everlasting",
    "Whimsical",
    "Baffling",
    "Zany",
    "Bizarre",
    "Eccentric",
    "Hilarious",
    "Bemusing",
    "Bewildering",
    "Curious",
    "Unconventional",
    "Enigmatic",
    "Puzzling",
    "Startling",
    "Surprising",
    "Wacky",
    "Extraordinary",
    "Oddball",
    "Preposterous",
    "Unbelievable",
    "Fanciful",
    "Unpredictable",
    "Wondrous",
    "Absurd",
    "Whacky",
    "Outlandish",
    "Ridiculous",
    "Silly",
    "Comical",
    "Farcical",
    "Inexplicable",
    "Offbeat",
    "Quizzical",
    "Rib-tickling",
    "Mind-boggling",
    "Surreal",
    "Hysterical",
    "Flabbergasting",
    "Laughter-inducing",
    "Giggle-worthy",
    "Astonishing",
    "Off-the-wall",
    "Chuckle-provoking",
    "Mind-bending",
    "Jaw-dropping",
    "Monty Python-esque",
    "Jocund",
    "Perplexing",
    "Bamboozling",
    "Whirligig",
    "Absurdist",
    "Befuddling",
    "Mirthful",
    "Kaleidoscopic",
    "Wunderbar",
    "Whimsy",
    "Kooky",
    "Flabbergasting",
    "Surreal",
    "Whizbang",
    "Puzzling",
    "Bamboozlement",
    "Wobbly",
    "Jaw-dropping",
    "Bewitching",
    "Boggling",
    "Zigzagging",
    "Gobbledygookish",
    "Flummoxing",
    "Shenanigans",
    "Rambunctious",
    "Hilarious",
    "Wiggly",
    "Absurdly funny",
    "Giggletastic",
    "Bizarro",
    "Kooky",
    "Zigzagging",
    "Curly",
    "Bonkers",
    "Ludicrous",
    "Freaky",
    "Befuddling",
    "Bamboozling",
    "Nonsensical",
    "Hysterical",
    "Whimsical",
    "Inexplicable",
    "Goofy",
    "Zigzagging",
    "Riotous",
    "Bizarre",
    "Baffling",
    "Flippity-floppity",
    "Wacky",
    "Zoinks",
    "Kaleidoscopic",
    "Zigzagging",
    "Quizzical",
    "Baffling",
    "Mystifying",
    "Astounding",
    "Flamboyant",
    "Startling",
    "Unbelievable",
    "Whacky",
    "Puzzling",
    "Bemusing",
    "Mind-blowing",
    "Far-out",
    "Hilarious",
    "Whimsy",
    "Boggle-worthy",
    "Intriguing",
    "Crazy",
    "Eccentric",
    "Hysterical",
    "Quirky",
    "Zippy",
    "Flummoxing",
    "Kooky",
    "Outrageous",
    "Mind-boggling",
    "Absurd",
    "Absurdly funny",
    "Zigzagging",
    "Baffling",
    "Whimsical",
    "Wunderbar",
    "Kooky",
    "Giggly",
    "Puzzling",
    "Curious",
    "Ridiculous",
    "Zany",
    "Silly",
    "Goofy",
    "Ludicrous",
    "Bizarre",
    "Unconventional",
    "Whacky",
    "Wibbly-wobbly",
    "Kaleidoscopic",
    "Merry",
    "Bamboozling",
    "Flabbergasting",
    "Mind-bending",
    "Zigzagging",
    "Bizarre",
    "Mirthful",
    "Outlandish",
    "Whimsy",
    "Kooky",
    "Zigzagging",
    "Wacky",
    "Quizzical",
    "Befuddling",
    "Unpredictable",
    "Kaleidoscopic",
    "Wibbly-wobbly",
    "Hilarious",
    "Absurd",
    "Zany",
    "Perplexing",
    "Whimsical",
    "Puzzling",
    "Flabbergasting",
    "Bamboozling",
    "Befuddling",
    "Whacky",
    "Ludicrous",
    "Nonsensical",
    "Bizarre",
    "Eccentric",
    "Hysterical",
    "Unconventional",
    "Curious",
    "Quirky",
    "Zigzagging",
    "Zany",
    "Ridiculous",
    "Bemusing",
    "Giggletastic",
    "Wobblewoppy",
    "Gadzooksian",
    "Brouhaha-ish",
    "Hootenanny-esque",
    "Wunderkindly",
    "Quizzical",
    "Nonsense",
    "Zonked",
    "Absurdly amusing",
    "Whimsy",
    "Jocund",
    "Flabbergasting",
    "Bewitching",
    "Gobbledygookish",
    "Freakishly funny",
    "Higgledy-piggledy",
    "Bamboozling",
    "Quizzical",
    "Sassafrassy",
    "Wibble-wobbly",
    "Hodgepodgey",
    "Pandemonious",
    "Bafflingly",
    "Flummoxing",
    "Wiggly-waggly",
    "Hilarious",
    "Wobbly",
    "Silly",
    "Bonkers",
    "Ludicrous",
    "Bewildering",
    "Ridiculous",
    "Wacky",
    "Giggly",
    "Whimsical",
    "Zigzagging",
    "Bamboozling",
    "Zany",
    "Quirky",
    "Mystifying",
    "Absurdly amusing",
    "Goofy",
    "Bizarre",
    "Farcical",
    "Eccentric",
    "Whacky",
    "Nonsensical",
    "Hysterical",
    "Unconventional",
    "Curious",
    "Zigzagging",
    "Puzzling",
    "Bemusing",
    "Bewildering",
    "Mirthful",
    "Absurd",
    "Quizzical",
    "Zippy",
    "Flummoxing",
    "Kooky",
    "Outrageous",
    "Mind-boggling",
    "Ridiculous",
    "Surreal",
    "Whimsical",
    "Giggly",
    "Zigzagging",
    "Quizzical",
    "Puzzling",
    "Bemusing",
    "Curious",
    "Hilarious",
    "Whimsy",
    "Boggle-worthy",
    "Intriguing",
    "Crazy",
    "Eccentric",
    "Hysterical",
    "Quirky",
    "Zippy",
    "Flummoxing",
    "Kooky",
    "Outrageous",
    "Mind-boggling",
    "Absurd",
    "Zigzagging",
    "Baffling",
    "Whimsical",
    "Wunderbar",
    "Kooky",
    "Giggly",
    "Puzzling",
    "Curious",
    "Ridiculous",
    "Zany",
    "Silly",
    "Goofy"
  ]  
  
  def getNoun(self):
    return random.choice(self.nounslist)
  
  def getAdjective(self):
    return random.choice(self.adjectiveslist)
  
  def getTemplate(self):
    return """
One day the {{noun}} went to see the {{noun}} at the park, and talked about {{noun}}s. They also bought a {{adjective}} {{adjective}} {{noun}} and a {{adjective}} {{noun}} from the {{noun}}, but that wasn't until after they ate the {{adjective}} {{noun}}.

The {{noun}} was shining brightly as the {{noun}} made their way to the park. {{adjective}} filled the air as they anticipated spending a {{adjective}} day in nature's embrace. As they arrived, the {{noun}} noticed the {{adjective}} beauty of the park, with its {{adjective}} {{noun}} and {{adjective}} {{noun}}s that adorned the landscape.

Eager to share their thoughts and experiences, the {{noun}} approached the {{noun}}, who was sitting on a bench, observing the surroundings. They sat down together, engaging in a {{adjective}} conversation about {{noun}}s. They discussed their favorite {{noun}}s, shared anecdotes, and exchanged {{adjective}} insights.

After their {{adjective}} conversation, they decided to explore the nearby food stalls. The aroma of {{adjective}} treats wafted through the air, enticing their senses. Among the array of options, a particular {{adjective}} {{adjective}} {{noun}} caught their attention. Its {{adjective}} smell and {{adjective}} presentation were too enticing to resist. They eagerly ordered it, savoring every {{adjective}} bite.

As they continued their culinary adventure, they stumbled upon a small vendor selling {{adjective}} handmade crafts. Their eyes lit up with {{adjective}} as they spotted a mesmerizing display of a {{adjective}} {{noun}}. Its {{adjective}} design and {{adjective}} colors immediately captivated their attention. Unable to resist its {{adjective}}, they decided to make it their own, knowing it would be a cherished addition to their collection.

Their exploration didn't end there. They also stumbled upon a stall showcasing a {{adjective}} piece of art—a {{adjective}} {{noun}}. Its {{adjective}} craftsmanship and {{adjective}} attention to detail left them in {{adjective}}. Enchanted by its {{adjective}}, they couldn't resist the urge to possess this {{noun}}, a true testament to the artist's {{noun}}.

After their {{adjective}} shopping experience, the {{noun}} and {{noun}} found a {{adjective}} spot under a {{adjective}} tree. They unwrapped the {{adjective}} {{noun}} they had purchased earlier. With each bite, they indulged in the {{adjective}} flavors that danced on their taste buds. The combination of {{noun}}s and the burst of flavors left them thoroughly satisfied.

As they savored the last morsels of their meal, they reflected on the {{adjective}} day they had shared. The park had been a {{noun}} for them, providing a respite from the {{adjective}} hustle and bustle. The bond they had forged over their shared interests had grown {{adjective}}, and their memories of this day would forever hold a {{adjective}} place in their hearts.

In conclusion, the day spent at the park was an {{adjective}} experience for the {{noun}}. From engaging in {{adjective}} conversations about {{noun}}s to indulging in {{adjective}} treats and acquiring {{adjective}} treasures, the day was filled with {{noun}} and discovery. It served as a reminder of the {{adjective}} pleasures that can be found in the company of a {{noun}}, the {{adjective}} of {{noun}}, and the {{adjective}} of exploring new experiences.

In the {{noun}} land of {{noun}}, there lived {{noun}} named {{noun}}. This {{noun}} had a knack for {{verb}}ing different genres of {{noun}}, creating concoctions that were {{adjective}}, {{adjective}}, and utterly {{adjective}}. One day, {{noun}} embarked on a {{adjective}} adventure that would {{verb}} together not just {{noun}} or {{noun}}, but {{noun}} different genres, promising an {{adjective}} {{noun}} like no other.

It all began on a {{adjective}} and {{adjective}} {{noun}} when {{noun}} {{verb}}ed upon a {{adjective}} {{noun}} hidden behind a {{noun}} of {{adjective}} {{noun}} in {{noun}} cluttered {{noun}}. {{noun}} got the better of {{noun}}, and without {{verb}}ing, {{noun}} {{verb}}ed into the {{noun}} {{verb}}, unaware of the {{adjective}} {{noun}} that awaited {{noun}}.

As {{noun}} {{verb}}ed from the {{noun}}, {{noun}} found {{noun}} in a {{noun}} filled with {{verb}}ing {{noun}}, {{verb}}ing {{noun}}, and {{adjective}} {{noun}}s. {{noun}} greeted {{noun}} with a mix of {{adjective}} {{noun}} and {{adjective}} {{noun}}, unable to {{verb}} this {{adjective}} {{noun}}. They were in desperate need of a {{noun}} to {{verb}} their {{noun}} from an {{adjective}} {{noun}}, and little did they know that {{noun}} would be the key to their {{noun}}.

Armed with {{noun}} trusty {{noun}} and clad in an {{adjective}} {{noun}}, {{noun}} {{verb}}ed off on a {{noun}} to {{verb}} a {{adjective}} crew of {{noun}}s. Along the way, {{noun}} encountered a {{adjective}} {{noun}} named {{noun}}, a {{adjective}} {{noun}} with a penchant for {{verb}}ing {{noun}}, and a {{verb}}ing {{noun}} with a voice that could {{verb}} {{noun}}.

Their {{noun}} took them through {{adjective}} {{noun}}, {{adjective}} {{noun}}, and even into {{adjective}} {{noun}}, as they {{verb}}ed {{adjective}} {{noun}}, {{verb}}ed {{adjective}} {{noun}}, and {{verb}}ed under a cascade of {{noun}}s. Each {{noun}} seamlessly {{verb}}ed into the next, creating a {{adjective}} narrative that kept everyone on their {{noun}}.

But it wasn't just {{noun}} and {{noun}} that awaited them. The group {{verb}}ed upon a {{adjective}} {{noun}} where the {{noun}} {{verb}}ed in a {{noun}} of {{noun}} and indulged in {{adjective}} {{noun}}. {{noun}} found {{noun}} caught in a {{adjective}} {{verb}}-off with a group of {{adjective}} {{noun}}, {{verb}}ing {{noun}} moves and leaving the {{noun}}s in {{noun}}.

As their {{noun}} reached its {{noun}}, {{noun}} {{verb}}ed off against the {{adjective}} {{noun}} in an {{adjective}} {{noun}} of {{noun}} and {{noun}}. With a {{adjective}} {{noun}} and a dash of {{adjective}} {{noun}}, {{noun}} outsmarted the {{noun}} and {{verb}}ed {{noun}} to the {{noun}} of the {{noun}}.

The {{noun}} concluded with a {{adjective}} {{noun}}, where the {{noun}} from each {{noun}} gathered for a {{adjective}} {{noun}}. There were {{adjective}} {{noun}}s {{verb}}ing alongside {{adjective}} {{noun}}s, and {{adjective}} {{noun}}s telling {{noun}}s to {{adjective}} {{noun}}s. {{noun}} echoed through the {{noun}} as {{noun}} stood at the center of it all, {{adjective}} in the {{noun}} that {{noun}} had {{verb}}ed a {{noun}} that would be remembered for {{noun}} to come.

And so, dear {{noun}}, the {{noun}} of {{noun}}'s {{noun}}-{{verb}}ing {{noun}} comes to an {{noun}}. It was a {{noun}} filled with {{adjective}} {{noun}}s, {{adjective}} {{noun}}s, and a whole lot of {{noun}}. May it serve as a {{noun}} that sometimes the most {{adjective}} {{noun}}s can {{verb}} us the {{adjective}} {{noun}} and {{verb}} us {{adjective}} {{noun}}s in the most {{adjective}} of {{noun}}s."""