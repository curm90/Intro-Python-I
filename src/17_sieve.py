def sieve_of_eratosthenes(n):
    non_prime = []
    for i in range(2, n):
        if i not in non_prime:
            print(i)
            for j in range(i * i, n, i):
                non_prime.append(j)


sieve_of_eratosthenes(100)
