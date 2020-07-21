# Gather prime factors, return as array
def prime_factors(n):
    primes = []
    steps = []
    # volatile var for storage of prime val
    p = 2
    # Repeatedly check against smallest prime divisors starting at 2
    # increment until all are found
    while n >= p*p:
        # determine divisibility by 'p'
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
#   Note: Positive Integers for a < b
def euclid_gcd(a, b):
    # Incremental steps
    print("%s divides %s" %(b, a))
    # Recursively call self if next step does not = 0 else return GCD
    return euclid_gcd(b%a, a) if (not b%a == 0) else a

#   Functionally identical to the above but does not print incremental steps.
#   written to experiment with lambda expressions
euclid_gcd_b = lambda a, b : euclid_gcd_b(b%a, a) if (not b%a == 0) else a

# uses return value of gcd to determine the LCM
# uses the lambda form of euclid_gcd so there are no annoying print statements
def lcm(a, b):
    x = euclid_gcd_b(a, b)
    print("LCM of %s and %s = %s" % (a, b, (a*b)//x))




#Test Cases
print("135: ", prime_factors(135))
print("*"*30)
print("75: ", prime_factors(75))
print("*"*30)
print("9145: ", prime_factors(9145))

print("*"*30)
print("GCD of 12, 140 = ",euclid_gcd(12, 140))
print("*"*30)
print("GCD of 73, 245 = ", euclid_gcd(73, 245))
print("*"*30)
print("GCD of 84, 1254 = ", euclid_gcd(84, 1254))

print("*"*30)
lcm(20, 50)
print("*"*30)
lcm(105, 43)
print("*"*30)
lcm(200, 13)