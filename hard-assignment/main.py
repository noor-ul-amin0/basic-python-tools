"""
Main entry point for the Hangman game.
"""
import os
import time
from hangman import HangmanGame, clear_screen
from words import get_words_by_category

def display_menu():
    """Display the main menu and get user choice."""
    clear_screen()
    print("\n===== HANGMAN GAME =====\n")
    print("1. Start New Game")
    print("2. Choose Word Category")
    print("3. How to Play")
    print("4. Quit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    return choice

def display_category_menu():
    """Display the category selection menu and get user choice."""
    clear_screen()
    print("\n===== SELECT WORD CATEGORY =====\n")
    print("1. Programming")
    print("2. Animals")
    print("3. Fruits")
    print("4. Countries")
    print("5. All Categories (Default)")
    print("6. Return to Main Menu")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    return choice

def display_how_to_play():
    """Display game instructions."""
    clear_screen()
    print("\n===== HOW TO PLAY HANGMAN =====\n")
    print("1. The computer selects a secret word")
    print("2. You need to guess the word one letter at a time")
    print("3. For each incorrect guess, a part of the hangman is drawn")
    print("4. You win if you guess the word before the hangman is complete")
    print("5. You lose if the hangman drawing is completed before you guess the word")
    print("\nYou have 6 incorrect guesses before the game ends.")
    
    input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    word_category = None
    category_name = "All Categories"
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            # Start new game
            words = get_words_by_category(word_category)
            game = HangmanGame(words)
            
            clear_screen()
            print(f"\nStarting new game with category: {category_name}")
            print("Try to guess the word before the hangman is complete.")
            time.sleep(2)
            
            game.play()
            
            play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
            if play_again != 'y':
                continue  # Return to main menu
            else:
                game.reset_game()
                continue
                
        elif choice == '2':
            # Choose word category
            category_choice = display_category_menu()
            
            if category_choice == '1':
                word_category = 'programming'
                category_name = "Programming"
            elif category_choice == '2':
                word_category = 'animals'
                category_name = "Animals"
            elif category_choice == '3':
                word_category = 'fruits'
                category_name = "Fruits"
            elif category_choice == '4':
                word_category = 'countries'
                category_name = "Countries"
            elif category_choice == '5':
                word_category = None
                category_name = "All Categories"
            
            if category_choice != '6':
                print(f"\nCategory set to: {category_name}")
                time.sleep(1.5)
                
        elif choice == '3':
            # How to play
            display_how_to_play()
            
        elif choice == '4':
            # Quit
            clear_screen()
            print("\nThanks for playing Hangman! Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            time.sleep(1.5)
