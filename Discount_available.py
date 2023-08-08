"""Write a Python program that takes two inputs from the user: "Is the customer a student?" (student) and "Is the customer a senior citizen?" (senior).
 If the customer is a student OR a senior citizen, the program should display "You are eligible for a discount!"
 Otherwise, it should display "No discount available."""

customer = input("What is your status: ")
#You're to check that they entered 'student'. So you're to compare the input entered matches 'student'
if customer == "student" or customer == "senior citizen":
  print("You are eligible for discount")
else:
  print("No discount available")
