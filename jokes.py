#Write a program that asks a user for their favourite number and then tells them a joke. The program will call a joke printing function with the users favourite number. 
#The function will accept one numeric parameter and use it to choose the joke to tell. You will probably use multi_selection if statement to match the joke against the number.

#define function 
def joke():

  #next input is jokeType
  jokeType = input("What type of joke are you in the mood for?\nEnter a for knock knock\nEnter b for cheese\n")

  #if statement for jokeType a
  if jokeType == "a":
    knockNum = int(input("Ok, now pick a number 1, 2 or 3.\n"))

    #embedded if for knockNum = 1
    if knockNum == 1:
      whosThere = input("Knock knock...\n")
      reply = input("Voodoo...\n")
      print ("Voodoo you think you are asking all these questions")

    #embedded if for knockNum = 2
    if knockNum == 2:
      whosThere = input("Knock knock...\n")
      reply = input("Scold...\n")
      print ("Scold outside, can you let me in please?")

    #embedded if for knockNum = 3
    if knockNum == 3:
      whosThere = input("Knock knock...\n")
      reply = input("Gladys...\n")
      print ("Gladys Friday.")

  #if statement for jokeType b
  if jokeType == "b":
    cheeseNum = int(input("Ok, now pick a number 1, 2 or 3.\n"))

    #embedded if for cheeseNum = 1
    if cheeseNum == 1:
      reply = input("What type of cheese do you use to entice a grizzly out of the forrest?\n")
      print ("Camembert")

    #embedded if for cheeseNum = 2
    if cheeseNum == 2:
      reply = input("What cheese is not your cheese?\n")
      print ("Nacho cheese")

    #embedded if for cheeseNum = 3
    if cheeseNum == 3:
      reply = input("What did the cheese say to himself in the mirrow?\n")
      print ("Halloumi")  

# function
joke()
