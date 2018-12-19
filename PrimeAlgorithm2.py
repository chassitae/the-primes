def getNum():
    number = int(input("Enter a number greater than 1: "))
    return number

def findPrimes(number):
    primes = []

    for x in range(2, number+1):
        if isPrime(x):
            primes.append(x)

    print(primes)

def isPrime(number):
    count = 0
    prime = False

    for x in range(2, number):
        if x == number:
            prime = True
        elif number % x == 0:
            count+=1

    if count == 0:
        prime = True

    return prime

def main():
    repeat = 'y'

    while repeat == 'y':
        number = getNum()
        findPrimes(number)
        isPrime(number)
        
        repeat = input("Try again? [y/n]:  ")

main()
