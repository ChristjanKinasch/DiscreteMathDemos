def convert_base(n, base_from, base_to):
    num_arr = []

    # recursive function, takes the number and the base to convert to
    def conv_down(n, b):
        # store the remainder in parent scoped array
        num_arr.append(n%b)
        # pass to next operation if n > 0, else remove last item (0)
        conv_down(n//b, b) if (n > 0) else num_arr.pop()
    
    def conv_up(n, b):
        print("up you go!")

    # handle conversion direction
    if base_from > base_to:
        conv_down(n, base_to)
        # reverse the list
        num_arr = num_arr[::-1]
        # combine list and return as whole integer value
        num_arr = [str(i) for i in num_arr]
        return "".join(num_arr)
    else:
        conv_up(n, base_to)

print(convert_base(2473, 10, 8))
print(convert_base(85, 10, 2))
print(convert_base(2017,10, 5))

#TODO: 
#   - upwards conversion function
#   - allow for systems > 10   
