"""

A program that prints out a list of all prime numbers
in the first n natural numbers / positive integers.

"""


# Creates a list of integers from 1 to n
n = 10
original = list(range(1, n + 1))

#print(original)

primes = []


for num in original:

    # Check if prime by checking all factors
    # Iterate through all numbers [2, num-1]
    # More efficiently, up to num // 2 + 1 (around half).

#    for i in range(2, num):
    for i in range(2, num // 2 + 1):
        remainder = num % i
        if remainder == 0:
            # Divisible; not prime, so break
            break
  
    else:  # Only activates if loop ended normally
        # If the loop did not break, then prime

        if num != 1:              # Checks for 1
            primes.append(num)

print(primes)