import time
import random

print("Let's play hangman")
word_bank = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
word = '''Insert code to randomly select a word from the word bank'''
# guesses is an empty string array that will be filled with letters guessed by the player
guesses = ''
turns = '''Determine the maximum number of attempts you want to give the player'''

# #check if the turns are more than zero to determine if the game is still running
while turns > 0:
    # Create a variable that determines if the game is won
    # Create a variable that determines if the player got a wrong guess
    # Check the characters in guesses

    # Create a for loop that goes through every char in the word variable
    # Check if char is in the guesses variable. If it is, print the char, if it isn't print an underscore
    # Check if the word is complete. If yes, set the game as won and break the loop

    # Print out the existing guesses
    # Create a variable called guess and have it take an input from the player
    # Append player guess to array

    # Determine if the guess isn't in the word. If it isn't, subtract 1 from the number of remaining turns
    # If turns = 0, set the game state as lost
