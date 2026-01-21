# diag1

# START

width: int = int(input("rectangle width?"))
height: int = int(input("rectangle height?"))

if width > 0 and height > 0:
    # YES
    print (width * height)
else:
    # NO
    print("invalid input")

# STOP


### print in red:
# diag1
'''
# START

width: int = int(input("rectangle width?"))
height: int = int(input("rectangle height?"))

RED = "\033[31m"

if width > 0 and height > 0:
    # YES
    print (width * height)
else:
    # NO
    print(f"{RED}invalid input")

# STOP
'''