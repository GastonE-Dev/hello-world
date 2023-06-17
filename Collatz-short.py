# First define the function with an argument

def collatz(n):
    if n % 2 == 0:
        return n // 2
    elif n % 2 == 1:
        return n * 3 + 1

print('Enter a number')
n = int(input())
while n != 1:
    n = collatz(n)
    print(n)

# This version shortens the argument "number" to just "n".
