def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Input a number from the user
num = int(input("Enter a number: "))

# Calculate the factorial and print the result
result = factorial(num)
print(f"The factorial of {num} is {result}")
