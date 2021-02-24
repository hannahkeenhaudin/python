###Write a program to ask a student for their percentage mark and convert this to a grade

#define program
def markGrade():

  #ask user for their %mark
  mark = (input("Please enter your percentage mark: \n"))

  #open while loop to test if entry is all digits. Will keep looping until entry is valid
  while mark.isdigit() is False:
    mark = (input("Invalid entry. Please enter your mark as a whole number not including the % symbol: \n"))
    
  #convert mark to integer
  mark = int(mark)

  #if statements to convert mark to grade
  if mark >= 90:
    grade = "A*"
  elif mark >= 80:
    grade = "A" 
  elif mark >= 70:
    grade = "B"
  elif mark >= 60:
    grade = "C"
  else:
    grade = "F"

  #ask for target mark
  targetGrade = input("Please enter your target grade: \n")

  #open while loop to check targetGrade is valid entry. Keep looping until it is
  while targetGrade != "A*" and targetGrade != "A" and targetGrade != "B" and targetGrade != "C" and targetGrade != "F":
    targetGrade = input("Invalid entry. Please enter either A*, A, B, C or F: \n")

  #print the target grade and grade
  print("Your target grade was " + targetGrade + " and your grade is " + grade)

  #if targetGrade and grade are the same print statement
  if targetGrade == grade:
    print ("Well done. You got your expected grade.\n")
  
  #if targetGrade was A* (and grade is not same as per previous if statement) print didn't make target
  elif targetGrade == "A*":
    print ("Unfortunately you didn't make your target grade.\n")
  
  #if target was A
  elif targetGrade == "A":
    if grade == "A*":
      print ("Amazing. You did even better than expected!\n")
    else:
      print ("Unfortunately you didn't make your target grade.\n")
  
  #if target was B
  elif targetGrade == "B":
    if grade == "A*" or grade == "A":
      print ("Amazing. You did even better than expected!\n")
    else:
      print ("Unfortunately you didn't make your target grade.\n") 

  #if target was C  
  elif targetGrade == "C":
    if grade == "A*" or grade == "A" or grade == "B":
      print ("Amazing. You did even better than expected!\n")
    else:
      print ("Unfortunately you didn't make your target grade.\n")
  
  #if target was F (and grade was higher as per first if statement)
  elif targetGrade == "F":
      print ("Amazing. You did even better than expected!\n")

#run program
markGrade()