# x = [[y for y in range(1,5,2)] for x in range(1,21 ) ]
# print(x)


## positional arguments and keyword arguments

def myfunction(c,a, b):
    print(f"a: {a}, b: {b}, c: {c}")

# Positional arguments
myfunction(1, 2, 3)

# Keyword arguments
myfunction(a=1, b=2, c=3)

# Mixed arguments (positional first, then keyword)
myfunction(1, b=2 , a=3) 


# Default arguments
def myfunction_with_defaults(a, b=2, c=3):
    print(f"a: {a}, b: {b}, c: {c}")

# Calling with only one argument, b and c will take default values
myfunction_with_defaults(1)

# Calling with two arguments, c will take the default value
myfunction_with_defaults(1, 4)

# Calling with all arguments, no default values will be used
myfunction_with_defaults(1, 4, 5)

myfunction_with_defaults(1, b=6,c=5)