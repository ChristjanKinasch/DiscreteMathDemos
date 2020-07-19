# Gather prime factors, return as array
#   Note: Positive Integers
def prime_factors(n):
    primes = []
    steps = []
    # volatile var for storage of prime val
    p = 2
    # Repeatedly check against smallest prime divisors starting at 2
    # increment until all are found
    while n >= p*p:
        # ascertain divisibility by 'p'
        if not n % p == 0:
            p+=1
        else:
            # t = temporary variable for appending comparitive val to 'n' in steps[]
            t=n
            # floor division
            n //= p
            # append prime to primes[], steps to steps[]
            primes.append(p)
            steps.append("%s divides %s with %s" % (p, t, n))

    # append the final value (is prime) of 'n'
    primes.append(n)

    # return primes[] & if steps[] = empty -> 'n' was prime, format return
    return primes, steps if (len(steps) > 0) else "%s is Prime" % n

#Greatest Common Divisor with Euclidean Algorithm
#   Note: Positive Integers for x < y
def euclid_gcd(x, y):
    # Incremental steps
    print("%s divides %s" %(y, x))
    # Recursively call self if next step does not = 0 else return GCD
    euclid_gcd(y%x, x) if (not y%x == 0) else print("GCD = %s" % x)

#   Functionally identical to the above function, does not print incremental steps. 
#   written to experiment with lambda expressions
# euclid_gcd = lambda x, y : euclid_gcd(y%x, x) if (not y%x == 0) else print("GCD = %s" % x)

#Test Cases
print("135: ", prime_factors(135))
print("*"*30)
print("75: ", prime_factors(75))
print("*"*30)
print("311: ", prime_factors(311))

print("*"*30)
euclid_gcd(12, 140)
print("*"*30)
euclid_gcd(73, 245)
print("*"*30)
euclid_gcd(84, 1254)