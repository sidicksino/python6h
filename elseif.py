Weight = int(input("Enter you Weight : "))
unit = (input("(L)bs or (K)g : "))

if unit.upper() == 'L':
    a = Weight * 0.45
    print (f"You are {a} kilos")
elif unit.upper() == 'K':
    a = Weight / 0.45
    print(f"Your are {a} pounds")