import random

#quantity = 0
#tense = ""

# quantity_singular = 1
# quantity_plural = 2

#tense = ["past", "present", "future"]

# tense_past = tense[0]
# tense_present = tense[1]
# tense_future = tense[2]

# Define the main function.

def main():
quantity = 0
tense = ""

sentence1 = make_sentence(quantity == 1, tense == "past")
print (sentence1)

sentence2 = make_sentence(quantity == 1, tense == "present")
print (sentence2)

sentence3 = make_sentence(quantity == 1, tense == "future")
print (sentence3)

sentence4 = make_sentence(quantity != 1, tense == "past")
print (sentence4)

sentence5 = make_sentence(quantity != 1, tense == "present")
print (sentence5)

sentence6 = make_sentence(quantity != 1, tense == "future")
print (sentence6)



def get_determiner(quantity):
"""Return a randomly chosen determiner. A determiner is
a word like "the", "a", "one", "some", "many".
If quantity is 1, this function will return either "a",
"one", or "the". Otherwise this function will return
either "some", "many", or "the".

Parameter
quantity: an integer.
If quantity is 1, this function will return a
determiner for a single noun. Otherwise this
function will return a determiner for a plural
noun.
Return: a randomly chosen determiner.
"""

if quantity == 1:
words = ["a", "one", "the"]
else:
words = ["some", "many", "the"]

# Randomly choose and return a determiner.
word = random.choice(words)
return word


def get_noun(quantity):
"""Return a randomly chosen noun.
If quantity is 1, this function will
return one of these ten single nouns:
"bird", "boy", "car", "cat", "child",
"dog", "girl", "man", "rabbit", "woman"
Otherwise, this function will return one of
these ten plural nouns:
"birds", "boys", "cars", "cats", "children",
"dogs", "girls", "men", "rabbits", "women"

Parameter
quantity: an integer that determines if
the returned noun is single or plural.
Return: a randomly chosen noun.
"""
nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman",
"birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

if nouns == ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]:
quantity == 1
elif nouns == ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]:
quantity != 1

# Randomly choose and return a noun.
noun = random.choice(nouns)
return noun


def get_verb(quantity, tense):
"""Return a randomly chosen verb. If tense is "past",
this function will return one of these ten verbs:
"drank", "ate", "grew", "laughed", "thought",
"ran", "slept", "talked", "walked", "wrote"
If tense is "present" and quantity is 1, this
function will return one of these ten verbs:
"drinks", "eats", "grows", "laughs", "thinks",
"runs", "sleeps", "talks", "walks", "writes"
If tense is "present" and quantity is NOT 1,
this function will return one of these ten verbs:
"drink", "eat", "grow", "laugh", "think",
"run", "sleep", "talk", "walk", "write"
If tense is "future", this function will return one of
these ten verbs:
"will drink", "will eat", "will grow", "will laugh",
"will think", "will run", "will sleep", "will talk",
"will walk", "will write"

Parameters
quantity: an integer that determines if the
returned verb is single or plural.
tense: a string that determines the verb conjugation,
either "past", "present" or "future".
Return: a randomly chosen verb.
"""

if tense == "past":
verbs = ["drank", "ate", "grew", "laughed", "thought",
"ran", "slept", "talked", "walked", "wrote"]
if tense == "present" and quantity == 1:
verbs == ["drinks", "eats", "grows", "laughs", "thinks",
"runs", "sleeps", "talks", "walks", "writes"]
if tense == "present" and quantity != 1:
"drink", "eat", "grow", "laugh", "think",
"run", "sleep", "talk", "walk", "write"
if tense == "future":
verbs == ["will drink", "will eat", "will grow", "will laugh", "will think",
"will run", "will sleep", "will talk", "will walk", "will write"]


# #Randomly choose and return a verb
verb = random.choice(verbs)
return verb


def make_sentence(quantity, tense):
"""Build and return a sentence with three words:
a determiner, a noun, and a verb. The grammatical
quantity of the determiner and noun will match the
number in the quantity parameter. The grammatical
quantity and tense of the verb will match the number
and tense in the quantity and tense parameters.
"""


determiner = get_determiner(quantity)
noun = get_noun(quantity)
verb = get_verb(quantity, tense)

if quantity == 1:
sentence =f"{determiner.capitalize()} {noun} {verb}."
elif quantity != 1:
sentence = f"{determiner.capitalize()} {noun} {verb}."

if tense == "past":
sentence =f"{determiner.capitalize()} {noun} {verb}."
if tense == "present" and quantity == 1:
sentence =f"{determiner.capitalize()} {noun} {verb}."
if tense == "present" and quantity != 1:
sentence =f"{determiner.capitalize()} {noun} {verb}."
if tense == "future":
sentence =f"{determiner.capitalize()} {noun} {verb}."

return sentence


# Start this program by
# calling the main function.
main()
