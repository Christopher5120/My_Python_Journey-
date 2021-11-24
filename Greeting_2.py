"""Asking for the name of the user and only greeting Alice and Bob with their names"""
na_me = input("Please, enter your name: ")
if na_me == "Alice" or na_me == "Bob":
    print("Hello, " + na_me + "!")
else:
    print("Oops! You cannot be greeted with your name")
