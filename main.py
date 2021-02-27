import random,string
name = input('enter a name').replace(' ','')
dob = input('enter date of birth in the format dd/mm/yyyy').strip().split('/')
print(dob)
password = []
extractint = random.randint(0,5)
extractdate = random.randint(0,2)
for i in name