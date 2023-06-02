# Collatz sequence ("Automate the boring stuff" Chapter 3 practice)

def collatz(number):

    # If number is even, divide by 2.
    if (number % 2 == 0):
        return number // 2

# If number is odd, multiply by 3 and add 1 (3n+1)
    else:
        return number * 3+1

# The following specifies number must be input as integer

while True:
    try:
        number = int(input("Enter a number: "))
        break

# The following exception happens if a non-integer is entered
    except ValueError:
        print("Please enter a valid integer")

# In the following, while number is not equal to 1, continue sequence

while (number !=1):
    number = collatz(number)
    print(number)
