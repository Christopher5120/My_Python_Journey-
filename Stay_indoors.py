"""
Write a Python program that takes the temperature as input. If the temperature is less than 0 degrees Celsius OR greater than 30 degrees Celsius, the program should display "Extreme weather conditions.
Stay indoors." Otherwise, it should display "Enjoy the day!"

"""

temperature = int(input("What is the temperature in degree celcius: "))
if temperature < 0 or temperature > 30:
  print("Stay Indoors")
else:
  print("Enjoy your day")
