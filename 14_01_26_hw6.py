
# START

'''
כתוב תוכנית בפייתון
שים בתא זיכרון pizza את מספר הפיצות שהוזמנו: 4
לכל פיצה 8 משולשים
יש במסיבה 5 אנשים
חשב באמצעות // כמה משולשים מקבל כל אורח
חשב באמצעות % כמה משולשים נשארו
'''

pizza: int = 4  # ordered 4 pizza
num_of_slices: int = 8
people = 5

each_guest: int = (pizza * num_of_slices) // people
remaining: int = (pizza * num_of_slices) % people

print('each guest gets', each_guest)
print('remaining', remaining)

# STOP