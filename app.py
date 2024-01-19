weight = int(input('Your weight: '))
kg_or_lbs = input('(K)g or (L)bs? ')

if kg_or_lbs.upper() == "K":
    converted = weight * 2.2
    print(f"You are {converted} lbs")
else:
    converted = weight / 2.2
    print(f"You are {converted} kilos")