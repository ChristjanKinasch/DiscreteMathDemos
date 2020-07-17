#Prime Factors, First approach
def prime_factors(x):
        return x-1
#Greatest Common Divisor & Lowest Common Multiple, First Approach
def gcd_lcm(x, y):
    return x+1, y-1

#Greatest Common Divisor with Euclidean Algorithm
def euclid_gcd(x, y):
    x_steps=[x]
    y_steps=[y]

    return format_output(x_steps, x), format_output(y_steps, y)

def format_output(steps, x):
    return format("Steps: %s \n Out: %s" %(steps, x))

#Test Cases
#print(prime_factors(92))
#print(prime_factors(109))
#print(prime_factors(315))

#print(gcd_lcm(82,92))
#print(gcd_lcm(104, 22))
#print(gcd_lcm(10294, 42))

#print(euclid_gcd(33, 89))
#print(euclid_gcd(912, 547))
#print(euclid_gcd(432, 91))