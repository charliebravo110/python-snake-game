#!/usr/bin/env python3
"""
Prime Number Calculator
Calculates and displays the first 50 prime numbers.
"""

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_first_n_primes(n):
    """
    Generate the first n prime numbers.
    
    Args:
        n (int): Number of primes to generate
        
    Returns:
        list: List of the first n prime numbers
    """
    primes = []
    candidate = 2
    
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    
    return primes

def main():
    """Main function to calculate and display the first 50 prime numbers."""
    print("Calculando los primeros 50 números primos...")
    print("=" * 50)
    
    # Calculate the first 50 prime numbers
    primes = get_first_n_primes(50)
    
    # Display the results in a formatted way
    print(f"Los primeros {len(primes)} números primos son:")
    print("-" * 50)
    
    # Print 10 numbers per line for better readability
    for i in range(0, len(primes), 10):
        line = primes[i:i+10]
        formatted_line = " ".join(f"{num:4d}" for num in line)
        print(f"{i+1:3d}-{min(i+10, len(primes)):3d}: {formatted_line}")
    
    print("-" * 50)
    print(f"El número primo más grande encontrado es: {primes[-1]}")
    print(f"Total de números primos calculados: {len(primes)}")

if __name__ == "__main__":
    main()
