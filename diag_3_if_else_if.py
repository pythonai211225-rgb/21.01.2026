

# START

a: int = int(input("a?"))
b: int = int(input("b?"))

if a > b:
    # YES
    print(a)
else:
    # NO
    if a == b:
        # YES
        print('equals', a)
    else:
        # NO
        print(b)

# STOP