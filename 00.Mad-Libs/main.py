Title = input("Title of your story: ")

temp = """
Once upon a time in a {Adjective} {Noun}, there lived a {adjective2} {Noun2} named {Name}. 
{Name} was known for being incredibly {Adverb} when it came to {Verb}. One {adjective3} day, 
{Pronoun} met a {Adjective4} {Animal} who said, "{Exclamation}! Let's play {Noun3}!"
{Name} agreed, and together, they had {adjective5} adventures. 
They even enjoyed a meal of {Food} while watching the {Adjective6} {Noun4} at {Place}.
{Name} learned that sometimes, the best adventures happen when you {Verb2} and enjoy the world around you.
"""

Adjective = input("Enter an Adjective: ")
Noun = input("Enter a Noun: ")
adjective2 = input("Enter an Ajectivess: ")
Noun2 = input("Enter a Noun: ")
Name = input("Enter a Name: ")
Adverb = input("Enter an Adverb: ")
Verb = input("Enter a Verb: ")
adjective3 = input("Enter an Adjective: ")
Pronoun = input("Enter a Pronoun: ")
Adjective4 = input("Enter an Adjective: ")
Animal = input("Enter an Animal: ")
Exclamation = input("Enter an Exclamation: ")
Noun3 = input("Enter a Noun: ")
adjective5 = input("Enter an Adjective: ")
Food = input("Enter a Food: ")
Adjective6 = input("Enter an Adjective: ")
Noun4 = input("Enter a Noun: ")
Place = input("Enter a Place: ")
Verb2 = input("Enter a Verb: ")

story = temp.format(
    Adjective=Adjective,
    Noun=Noun,
   adjective2=adjective2, 
    Noun2=Noun2, 
    Name=Name,
    Adverb=Adverb,
    Verb=Verb,
    adjective3=adjective3, 
    Pronoun=Pronoun,
    Adjective4=Adjective4,
    Animal=Animal,
    Exclamation=Exclamation,
    Noun3=Noun3,
    adjective5=adjective5,
    Food=Food,
    Adjective6=Adjective6,
    Noun4=Noun4,
    Place=Place,
    Verb2=Verb2,
)

print(Title)
print(story)

