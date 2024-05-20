from random import choice
from words import word_list
import art

stages = art.stages
word = choice(word_list)
lives = 6
guesses = []
wrong_guesses = []
print(art.logo)
while True:
  for letter in word:
    if letter in guesses:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  guess = input("\nEnter a guess: ")
  if (guess in word and guess not in guesses):
    guesses.append(guess)
  elif guess in guesses or guess in wrong_guesses:
    print("You already guessed that letter!")
  else:
    wrong_guesses.append(guess)
    lives -= 1

  if len(guesses) == len(set(word)):
    print("You win!")
    break
  print(stages[lives])
  if lives == 0:
    print(f"The word was {word} Better luck next time!")
    break
