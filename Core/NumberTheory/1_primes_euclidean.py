# Ascertain prime factors, return as array
def prime_factors(n):
    primes=[]
    steps=[]
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
            n //= p
            # append prime to primes[], steps to steps[]
            primes.append(p)
            steps.append("%s divides %s with %s" % (p, t, n))

    # append the final value (is prime) of 'n'
    primes.append(n)

    # return primes[] & if steps[] = empty -> 'n' was prime, format return
    return primes, steps if (len(steps) > 0) else "%s is prime" % n

#Greatest Common Divisor & Lowest Common Multiple, First Approach
def gcd_lcm(x, y):
    xprimes = prime_factors(x)[0]
    yprimes = prime_factors(y)[0]

    

    return xprimes, yprimes

#Greatest Common Divisor with Euclidean Algorithm
def euclid_gcd(x, y):
    x_steps=[x]
    y_steps=[y]

    return format_output(x_steps, x), format_output(y_steps, y)

def format_output(steps, x):
    return format("Steps: %s \n Out: %s" %(steps, x))

#Test Cases
#print(prime_factors(92))
#print(prime_factors(655168))
#print(prime_factors(109))
#print(prime_factors(315))
#print(prime_factors(5043))

print(gcd_lcm(82,92))
#print(gcd_lcm(104, 22))
#print(gcd_lcm(10294, 42))

#print(euclid_gcd(33, 89))
#print(euclid_gcd(912, 547))
#print(euclid_gcd(432, 91))