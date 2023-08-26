# 9.5 - Challenge: Wax Poetic
# Solution to challenge


# Generate a random poem based on a set structure

import random

noun = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verb = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles",
]
adjective = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
]
preposition = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverb = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously",
]


def give_me_some(lst, num):
    """return a list made of num element of a given list, ensuring there are no duplicates"""
    result = []

    for i in range(num):
        picked = random.choice(lst)
        # We ensure that this element was not picked already
        while picked in result:
            picked = random.choice(lst)
        result.append(picked)
    return result


def right_article(adj):
    """Depending of the first letter of a given article, send back article a or an"""
    vowel = ("a", "e", "i", "o", "u")
    if adj[0] in vowel:
        return "an"
    else:
        return "a"


def make_poem():
    """Create a randomly generated poem, returned as a multi-line string."""
    # Pull nouns, verbs, adj, prep and adv as requested
    nouns = give_me_some(noun, 3)
    verbs = give_me_some(verb, 3)
    adjectives = give_me_some(adjective, 3)
    prepositions = give_me_some(preposition, 2)
    adv = give_me_some(adverb, 1)

    # Prepare the right articles
    first_article = right_article(adjectives[0])
    second_article = right_article(adjectives[2])
    
    # Create the poem
    poem = (
        f"{first_article.capitalize()} {adjectives[0]} {nouns[0]}"
        f"\n\n{first_article.capitalize()} {adjectives[0]} {nouns[0]} {verbs[0]} {prepositions[0]} the {adjectives[1]} "
        f"{nouns[1]}\n{adv[0]}, the {nouns[0]} {verbs[1]}"
        f"\nthe {nouns[1]} {verbs[2]} {prepositions[1]} {second_article} {adjectives[2]} {nouns[2]}"
        )

    return poem


poem = make_poem()
print(poem)
