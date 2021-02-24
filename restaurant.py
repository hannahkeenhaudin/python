#1. Write a program that allows user to enter his favourite starter, main course, dessert and drink. Output a message which says – “Your favourite meal is .........with a glass of....”

#define method and open
def restaurant():
  #next input is string greeting (with next line)
  greeting = input("Would you like to go for dinner tonight? y or n\n")

  #open if statement
  if greeting == "y":

  #next inputs are strings starter, main, dessert
    starter = input("Great. I have to pre order. What would you like to start?\n")
    main = input("Yum. And how about your main?\n")
    dessert = input("And for dessert?\n")
    #ask whether want to drink
    drinkYorN = input("And are we getting pissed? y or n\n")

    #imbedded if statement
    if drinkYorN == "y":
      drink = input("Right answer. What are we having?\n")
    #with imbedded else
    else:
      drink = input("You still drunk from last night? No worries. Still or sparking water then?\n")
  
    print ("Great. I'm excited already. So to confirm, you're having",starter,"to start. Then",main,"for your main and",dessert,"for pudding. And we're drinking",drink,". See you later.\n")

  #when if condition is not met go to else statement
  else:
    print ("Ok, have a nice evening anyway.\n")

#run the method
restaurant()
