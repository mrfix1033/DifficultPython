numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [numbers[p] for p in range(len(numbers)) if [all((i % o for o in range(2, int(i ** .5 + 1)))) if i > 1 else False for i in numbers][p]]
print(primes)
