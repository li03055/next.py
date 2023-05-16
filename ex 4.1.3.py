def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



def first_prime_over(n):
    prime_generator = (number for number in range(n + 1, 10 ** 10) if is_prime(number))
    for number in prime_generator:
        return number

print(first_prime_over(10000003))