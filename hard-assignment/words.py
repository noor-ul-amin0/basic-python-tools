"""
Word lists for the Hangman game.
This module provides different categories of words for the Hangman game.
"""

# Basic categories of words
PROGRAMMING_WORDS = [
    "python", "javascript", "algorithm", "function", "variable",
    "class", "object", "method", "inheritance", "polymorphism",
    "encapsulation", "database", "framework", "library", "interface",
    "compiler", "interpreter", "syntax", "semantic", "debug",
    "exception", "iteration", "recursion", "parameter", "argument"
]

ANIMALS = [
    "elephant", "giraffe", "penguin", "kangaroo", "zebra",
    "dolphin", "leopard", "octopus", "rhinoceros", "squirrel",
    "tiger", "panther", "koala", "gorilla", "cheetah",
    "alligator", "butterfly", "flamingo", "hedgehog", "jaguar"
]

FRUITS = [
    "apple", "banana", "orange", "strawberry", "pineapple",
    "watermelon", "grape", "mango", "kiwi", "blueberry",
    "peach", "cherry", "apricot", "avocado", "blackberry",
    "coconut", "cranberry", "papaya", "pomegranate", "raspberry"
]

COUNTRIES = [
    "australia", "brazil", "canada", "denmark", "egypt",
    "france", "germany", "hungary", "india", "japan",
    "kenya", "luxembourg", "mexico", "netherlands", "pakistan",
    "qatar", "russia", "singapore", "thailand", "ukraine"
]

# Combined list from all categories
ALL_WORDS = PROGRAMMING_WORDS + ANIMALS + FRUITS + COUNTRIES

def get_words_by_category(category=None):
    """
    Get a list of words based on the specified category.
    
    Args:
        category (str, optional): Category name. Options: 'programming', 'animals',
                                'fruits', 'countries', or None for all words.
    
    Returns:
        list: List of words from the specified category or all words if no category is specified.
    """
    category = category.lower() if category else None
    
    if category == 'programming':
        return PROGRAMMING_WORDS
    elif category == 'animals':
        return ANIMALS
    elif category == 'fruits':
        return FRUITS
    elif category == 'countries':
        return COUNTRIES
    else:
        return ALL_WORDS
