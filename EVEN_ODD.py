

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

even_count = 0
odd_count = 0
prime_count = 0


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if is_prime(n):
        prime_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Prime numbers:", prime_count)
