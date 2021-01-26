def is_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


assert is_prime(7) is True, "7 is prime number"
assert is_prime(10) is False, "10 is not a prime number"

# corner case test, which will catch error in is_prime function
assert is_prime(1) is False, "1 is not a prime number"
