"""
Write a Python program that asks the user to enter a password. If the password matches "Secret123," the program should display "Access granted."
Otherwise, it should display "Access denied."

"""

password = input("Enter password: ")
correct_password = "Secret123"

#This is good - Use this same approach for the questions above!

if password == correct_password:
  print("Access granted")
else:
  print("Access denied. Try again!")
