# Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


a ,b , c = 0, 1, 0
x = 0
while c < 4000000:
    c = a + b
    a, b = b, c
    if a % 2 == 0:
        x = x + a 
        print(x)
