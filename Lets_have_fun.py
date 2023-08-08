"""Write a Python program that takes two inputs from the user: "Is it Saturday?" (sat) and "Is it Sunday?" (sun). If either of these inputs is true, the program should display "Let's have fun!" Otherwise, it should display "Weekdays are for work."
"""

day = input("what day is today: ")
if day == "sat" or day == "sun":
  print("Let's have fun")
else:
  print("Weekdays are for work")
