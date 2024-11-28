numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n in numbers:
    if n == 1:
        continue
    is_prime = True
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            not_primes.append(n)
            is_prime = False
            break
    if is_prime:
        primes.append(n)

print(primes)
print(not_primes)