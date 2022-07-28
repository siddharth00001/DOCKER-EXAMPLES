n = int(input("Please enter any positive number: "))

if n<=0:
    print("error: Number is less than zero")
else:
    sum = 0
    i=n
    while i>0:
        sum+=i
        i -= 1
    print("Sum of all positive numbers till",n,"is",sum)