"""Accepting an input of an integer and finding the sum of the set of numbers from 1 to the input"""
num_ber = int(input("Enter a number: "))
num_ber1 = list(range(num_ber+1))
num_ber2 = sum(num_ber1)
print(num_ber2)
