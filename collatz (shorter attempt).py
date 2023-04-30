def collatz(n):
    if (n % 2 == 0):
        return (n // 2)
    else:
        return (n * 3+1)

print('Choose a number, mofo!')
n = int(input())
while (n != 1):
    n = collatz(n)
    print(n)
