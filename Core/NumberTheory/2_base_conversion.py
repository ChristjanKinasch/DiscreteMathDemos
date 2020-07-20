# takes number to convert 'n'; base from 'ba'; base to 'bb'
def convert_base(n, ba, bb):
    # replace numerals with alphabetic digits for systems > 10
    # add letters for higher bases
    overflow = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    overflow += ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
    # array for storing remainders; variable for final output
    num_arr, f = [], ""

    # recursive function, takes the number and the base
    def convert(n, b):
        # store remainder, use letters if required
        num_arr.append(n%b if n%b < 10 else overflow[(n%b)-10])
        # pass to next operation if n > 0, else remove last item (0)
        convert(n//b, b) if (n > 0) else num_arr.pop()

    # to convert between non-decimal systems, first convert to decimal
    def to_dec(n, b):
        # convert 'n' to array
        dig_arr = [int(i) for i in str(n)]
        # for processing loop
        arr_len = len(dig_arr)
        # final value
        f = 0
        for i in range(arr_len, 0, -1):
            # Multiply integer values in 'dig_arr" reverse order with factors of 10
            # sum in 'f'
            f+=dig_arr[arr_len-i] * (b**(i-1))
        return f
    
    # convert to decimal if not
    if(not ba == 10):
        n = to_dec(n, ba)

    # call recursive function
    convert(n, bb)
    # Combine num_arr in reverse order and return value    
    for i in range(len(num_arr), 0, -1):
            f+=str(num_arr[i-1])
    return f
    
print(convert_base(257, 10, 2))     # expect: 10 000 00 01
print(convert_base(257, 10, 5))     # expect: 2012
print(convert_base(192, 10, 3))     # expect: 21010
print(convert_base(192, 10, 7))     # expect: 363
print(convert_base(1506, 10, 11))   # expect: 114a
print(convert_base(1506, 11, 3))   # expect: 2122221
print(convert_base(3995, 10, 12))   # expect: 238b
print(convert_base(6841681, 10, 27))   # expect: cng0g
print(convert_base(122, 3, 7))   # expect: 23
print(convert_base(162, 7, 10))   # expect: 93