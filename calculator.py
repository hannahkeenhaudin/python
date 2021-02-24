#Write a program which will: Ask for two numbers. Then offers a menu to the user giving them a choice of operator e.g. – Enter “a” if you want to add “b” if you want to subtract Etc. Include +, -, /, *, **(to the power of) and square.

#define my function
def calculator():

  #cast inputs to floats to get two float inputs
  num1 = float(input("Please enter your first number:\n"))
  num2 = float(input("Now please enter your second number:\n"))

  #next input is choice
  choice = input("Would you like to:\na - add your numbers.\nb - subtract your numbers.\nc - multiply your numbers.\nd - divide your numbers.\ne - multiply by the power of.\nf - square.\n")

  #open if and elif statements for choice 
  if choice == "a":
    print (num1, "plus", num2, "is", num1+num2)
  elif choice == "b":
    print (num1, "take away", num2, "is", num1-num2)
  elif choice == "c":
    print (num1, "multiplied by", num2, "is", num1*num2)
  elif choice == "d":
    print (num1, "divided by", num2, "is", num1/num2)
  elif choice == "e":
    print (num1, "muliplied by the power of", num2, "is", num1**num2)
  elif choice == "f":
    print (num1, "squared is", num1**2, "and", num2, "squared is", num2**2)
  # and else in case of invalid entry
  else:
    print("Invalid entry")

#run funcation
calculator()
