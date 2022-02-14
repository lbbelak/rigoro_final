from math import sqrt
from itertools import count

SMALL_PRIMES = [2, 3, 5, 7, 11, 13]


def check_palindrome(number: int) -> bool:
    if str(number) == str(number)[::-1]:
        return True
    return False


def is_prime_and_palindrome(number: int) -> bool:
    if number in SMALL_PRIMES:
        return True
    if number % 2 == 0 or number == 1:
        return False
    for div in range(3, int(sqrt(number)) + 1, 2):
        if number % div == 0:
            return False
    if check_palindrome(number):
        return True
    return False


if __name__ == "__main__":
    num = input("Enter number:")
    try:
        int(num)
        is_num = True
    except ValueError:
        is_num = False
    if not is_num:
        print("Invalid input!")
    else:
        num = int(num)
        next_prime = next(filter(is_prime_and_palindrome, count(num)))
        print(next_prime)

