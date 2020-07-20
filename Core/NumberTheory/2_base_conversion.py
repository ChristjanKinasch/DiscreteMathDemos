# takes number to convert 'n'; base from 'ba'; base to 'bb'
def convert_base(n, ba, b):
    # replace numerals with alphabetic digits for systems > 10
    # add letters for higher bases
    overflow = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    # array for storing remainders; variable for final output
    num_arr, f = [], ""

    # recursive function, takes the number and the base
    def convert(n, b):
        # store remainder, use letters if required
        num_arr.append(n%b if n%b < 10 else overflow[(n%b)-10])
        # pass to next operation if n > 0, else remove last item (0)
        convert(n//b, b) if (n > 0) else num_arr.pop()

    # call recursive function
    convert(n, b)
    # Combine num_arr in reverse order and return value    
    for i in range(len(num_arr), 0, -1):
            f+=str(num_arr[i-1])
    return f
    
print(convert_base(257, 10, 2))     # expect: 10 000 00 01
print(convert_base(257, 10, 5))     # expect: 2012
print(convert_base(257, 10, 8))     # expect: 401
print(convert_base(192, 10, 3))     # expect: 21010
print(convert_base(192, 10, 7))     # expect: 363
print(convert_base(1506, 10, 11))   # expect: 114a
print(convert_base(3995, 10, 12))   # expect: 238b
print(convert_base(3995, 10, 19))   # expect: b15
print(convert_base(56566512, 10, 27))   # expect: b15