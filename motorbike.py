#2. A motorbike costs £2000 and loses 10% of its value every year. Print the bike’s value every year until it falls below £1000.

#define method
def motorbike():

  year = 2020

  #cost is next float input (cast to float)
  price = float(input("How much does the bike cost?\n"))

  #while price is above or equal to 1000, add 1 onto the year and take of 10% off price and print the new year and price
  while price >= 1000.00:
    year = year + 1
    price = price * 0.9
    print ("In", year, "the bike will cost:\n", price)

#run method
motorbike()
