#Give the user 6 chances to guess the computer's number. Tell the user if their guess is too high or too low

print ("\nHomework: Guessing game - Give the user 6 chances to guess the computer's number. Tell the user if their guess is too high or too low.\n")

# import to use random function
import random

#define program
def guessingGame():
  
  # the string userName will be inputted after the question
  userName = input("Hello, what is your name?\n")

  #random number is generated (1 to 100)
  number = random.randint(1,100)

  # print userName with string
  print ("Hello " + userName + " I am thinking of a number between 1 and 100.")

  #set number of guesses at 6
  numberOfGuesses = 6

  # the integer guess will be inputted after the question
  print ("Do you think you can guess it? I'll give you", numberOfGuesses, "guesses.")

  #open while loop for 6 guesses
  while numberOfGuesses > 0 :

    #next input is integer guess
    guess = int(input("Take a guess: "))
    
    #take one off number of guesses
    numberOfGuesses = numberOfGuesses-1
  
    #if guess is correct
    if guess == number:
      print("Well done, you got it! Thanks for playing")
      break #exit loop if guess if correct
    #if guess if greater than number
    if guess > number:
      print ("Sorry, that's too high. You have", numberOfGuesses, "guesses left.")
    #if guess if less than number
    if guess < number:
      print ("Sorry, that's too low. You have", numberOfGuesses, "guesses left.")  

  #if user runs out of guesses AND didn't guess the number correctly print the number
  if numberOfGuesses==0 and guess!=number:
    print ("Sorry, you didn't get it in six guesses. I was thinking of", number, ". Thanks for playing.")
  
#run program
guessingGame()
