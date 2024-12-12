def is_prime(num):
    # Check if num is greater than 1
    if num <= 1:
        return False
    # Check all possible divisors from 2 up to square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    # If no divisors found, num is prime
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
