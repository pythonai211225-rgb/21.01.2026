

# START

age: int = int(input("whats your age?"))

while age <= 0 or age >= 120:
    # YES
    age = int(input("whats your age?"))

    # ...
    # --> JUMP
else:
    print ('your age is', age)

# STOP