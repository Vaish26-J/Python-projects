fromCountry = input('enter a from country')
toCountry = input('enter a to country')
amt = float(input('enter the amount'))
fromCountry = fromCountry.strip().lower()
toCountry = toCountry.strip().lower()
convertedamt = 0
def inrtodlr(amt):
    return amt*0.0137130
def dlrtoinr(amt):
    return amt*72.925
if fromCountry == 'india' and toCountry == 'us':
    convertedamt = inrtodlr(amt)
    print('amount in us dollars:'+str(convertedamt))
elif fromCountry == 'us' and toCountry == 'india':
    convertedamt = dlrtoinr(amt)
    print('amount in indian rupee:'+str(convertedamt))