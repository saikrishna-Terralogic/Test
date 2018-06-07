# Program to find a factorial of a number

number = int(input("Enter an integer for finding factorial : "))
factorial = 1
for i in range(1, int(number)+1):
    factorial = i*factorial
print("factorial : ", factorial)
