''' Write a Java program to check if a given integer is a prime number. A prime number is a number that is only divisible by 1 and itself.
Expect :
Input : 7
Output : 7 is a prime number

Input : 10
Output : 10 is not a prime number '''


def prompt():
    while True:
        number = input("Number: ")
        if not number.isdigit() or len(number) == 0:
            print("Only enter digit")
            continue
        elif int(number) < 2:
            print("Number must be greater than 1")
            continue
        number = int(number)
        return number


def prime(n):
    divisor = [i for i in range(2, n-1)]
    for i in divisor:
        if n % i == 0:
            print(f'{n} is not a prime number')
            return
    print(f'{n} is a prime number')
    return


def main():
    number = prompt()
    prime(number)


main()