import re
from collections import Counter

def count_word_frequency(filepath):
    """
    Reads a text file and counts the frequency of each word.

    Args:
        filepath (str): The path to the text file.

    Returns:
        dict: A dictionary where keys are words and values are their frequencies.
    """
    try:
        with open(filepath, 'r') as file:
            text = file.read()
            
        # Remove punctuation and convert to lowercase to get accurate word counts
        words = re.findall(r'\b\w+\b', text)
        
        # Create a dictionary with word frequencies
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
                
        return word_freq
        
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}