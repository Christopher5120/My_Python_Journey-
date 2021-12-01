def calculate(n, power):
    return sum([int(i) for i in str(pow(n,power))])

n = 2
power = 1000

print(calculate(n,power))

