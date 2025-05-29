"""
Hangman Game

A simple text-based implementation of the classic Hangman word guessing game.
The player needs to guess a word letter by letter before the hangman is complete.
"""
import random
import os
import time


class HangmanGame:
    """
    Hangman game class that handles all game logic and display.
    """
    # ASCII art for hangman stages
    HANGMAN_STAGES = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        """
    ]

    def __init__(self, word_list=None):
        """
        Initialize the hangman game.
        
        Args:
            word_list (list, optional): List of words to choose from. 
                                        If None, a default list is used.
        """
        # Default word list if none is provided
        self.default_words = [
            "python", "hangman", "computer", "programming", "keyboard",
            "developer", "challenge", "algorithm", "function", "variable",
            "string", "integer", "dictionary", "list", "tuple", "module",
            "package", "object", "class", "method", "attribute", "inheritance",
            "polymorphism", "encapsulation", "abstraction", "exception"
        ]
        
        self.word_list = word_list if word_list else self.default_words
        self.reset_game()
    
    def reset_game(self):
        """Reset the game with a new word and clear previous game state."""
        self.word = random.choice(self.word_list).lower()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect = len(self.HANGMAN_STAGES) - 1
        self.game_over = False
        self.won = False
    
    def display_word(self):
        """
        Display the word with underscores for letters not yet guessed.
        
        Returns:
            str: The word display string (e.g., "p _ t h _ n")
        """
        display = []
        for letter in self.word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)
    
    def display_game_state(self):
        """Display the current state of the game."""
        clear_screen()
        print("\nHANGMAN GAME\n")
        print(self.HANGMAN_STAGES[self.incorrect_guesses])
        print(f"\nWord: {self.display_word()}")
        print("\nGuessed letters:", " ".join(sorted(self.guessed_letters)) if self.guessed_letters else "None")
        print(f"Incorrect guesses: {self.incorrect_guesses}/{self.max_incorrect}")
    
    def make_guess(self, letter):
        """
        Process a player's guess.
        
        Args:
            letter (str): The letter guessed by the player.
            
        Returns:
            bool: True if the guess was correct, False otherwise.
        """
        letter = letter.lower()
        
        # Check if letter has already been guessed
        if letter in self.guessed_letters:
            return None
        
        # Add to guessed letters
        self.guessed_letters.add(letter)
        
        # Check if letter is in the word
        if letter in self.word:
            # Check if all letters have been guessed
            if all(letter in self.guessed_letters for letter in self.word):
                self.won = True
                self.game_over = True
            return True
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= self.max_incorrect:
                self.game_over = True
            return False
    
    def play(self):
        """Main game loop."""
        while not self.game_over:
            self.display_game_state()
            
            # Get player input
            guess = input("\nGuess a letter: ").strip()
            
            # Validate input
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter.")
                time.sleep(1.5)
                continue
            
            result = self.make_guess(guess)
            
            if result is None:
                print(f"You've already guessed '{guess}'!")
                time.sleep(1.5)
            elif result:
                print("Good guess!")
                time.sleep(1)
            else:
                print("Incorrect!")
                time.sleep(1)
        
        # Final game state
        self.display_game_state()
        
        if self.won:
            print(f"\nCongratulations! You've won! The word was '{self.word}'.")
        else:
            print(f"\nGame over! The word was '{self.word}'.")


def clear_screen():
    """Clear the console screen."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')


def main():
    """Main function to run the Hangman game."""
    game = HangmanGame()
    
    while True:
        game.play()
        
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing Hangman! Goodbye!")
            break
        
        game.reset_game()


if __name__ == "__main__":
    main()
