# Program to find a factorial of a number

num = int(input("Enter an integer for finding factorial : "))
fact = 1
for i in range(1, int(num)+1):
    fact = i*fact
print("factorial : ", fact)
