# Hangman Game

A command-line implementation of the classic Hangman word guessing game.

## Features

- **Multiple Word Categories**: Choose from Programming, Animals, Fruits, or Countries
- **Interactive UI**: Visual representation of the hangman figure
- **User-friendly Interface**: Clear menus and navigation
- **Game Statistics**: Track incorrect guesses and display game progress

## How to Play

1. Run the game by executing `python main.py`
2. Navigate the menu to choose a word category or start a game
3. Guess one letter at a time
4. Try to guess the complete word before the hangman is fully drawn (6 incorrect guesses)

## Game Rules

- For each incorrect guess, a part of the hangman figure is drawn
- You win if you guess all the letters in the word before the hangman is complete
- You lose if the hangman is completely drawn before you guess the word

## Files

- `main.py`: Entry point and menu system
- `hangman.py`: Core game logic and display
- `words.py`: Word lists categorized by themes

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Example

```
===== HANGMAN GAME =====

1. Start New Game
2. Choose Word Category
3. How to Play
4. Quit

Enter your choice (1-4): 1

Starting new game with category: All Categories
Try to guess the word before the hangman is complete.

HANGMAN GAME

+---+
|   |
    |
    |
    |
    |
=========

Word: _ _ _ _ _ _

Guessed letters: None
Incorrect guesses: 0/6

Guess a letter:
```
