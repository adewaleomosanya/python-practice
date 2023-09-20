Title = input("Title of your story: ")

temp = """
Once upon a time in a {Adjective} {Noun}, there lived a {Adjectivess} {Noun} named {Name}. 
{Name} was known for being incredibly {Adverb} when it came to {Verb}. One {adjective} day, 
{Pronoun} met a {Adjectives} {Animal} who said, "{Exclamation}! Let's play {Noun}!"
{Name} agreed, and together, they had {adjectives} adventures. 
They even enjoyed a meal of {Food} while watching the {Adjectiv} {Noun} at {Place}.
{Name} learned that sometimes, the best adventures happen when you {Verb} and enjoy the world around you.
"""

Adjective = input("Enter an Adjective: ")
Noun = input("Enter a Noun: ")
Adjectivess = input("Enter an Ajectivess: ")
Non = input("Enter a Noun: ")
Name = input("Enter a Name: ")
Adverb = input("Enter an Adverb: ")
Verb = input("Enter a Verb: ")
adjective = input("Enter an Adjective: ")
Pronoun = input("Enter a Pronoun: ")
Adjectives = input("Enter an Adjective: ")
Animal = input("Enter an Animal: ")
Exclamation = input("Enter an Exclamation: ")
Nun = input("Enter a Noun: ")
adjectives = input("Enter an Adjective: ")
Food = input("Enter a Food: ")
Adjectiv = input("Enter an Adjective: ")
Nouns = input("Enter a Noun: ")
Place = input("Enter a Place: ")
Verbs = input("Enter a Verb: ")

story = temp.format(
    Adjective=Adjective,
    Noun=Noun,
    Adjectivess=Adjectivess,
    Non=Non, 
    Name=Name,
    Adverb=Adverb,
    Verb=Verb,
    adjective=adjective, 
    Pronoun=Pronoun,
    Adjectives=Adjectives,
    Animal=Animal,
    Exclamation=Exclamation,
    Nun=Nun,
    adjectives=adjectives,
    Food=Food,
    Adjectiv=Adjectiv,
    Nouns=Nouns,
    Place=Place,
    Verbs=Verbs,
)

print(Title)
print(story)

