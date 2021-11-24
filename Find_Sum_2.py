"""Accepting an input and finding the sum of only the prime numbers within the set"""
num_ber = int(input("Enter a number: "))
num_ber1 = (range(num_ber+1))
sum_d = 0
for x in num_ber1:
    if x % 3 == 0 or x % 5 == 0:
        sum_d = sum_d + x
    else:
        continue

print(sum_d)
