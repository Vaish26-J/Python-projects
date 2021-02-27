choice=input('enter the number of one of these choices.\n 1.Food\n 2. game\n 3.Tourism')
if choice == '1':
    f = open('food')
elif choice == '2':
    f = open('game')
elif choice == '3':
    f = open('tourism')
else:
  print('enter a valid choice (1,2,3)')
madLine = f.readline()
parts = madLine.split('#')
inputs = parts[0].split(',')
madText = parts[1]
store = ['']
for text in inputs:
    store.append(input('Enter '+text+':'))
for i in range(len(store)):
    madText = madText.replace('%'+str(i),store[i])
print(madText)
if choice == '1':
    f.close()
elif choice == '2':
    f.close()
elif choice == '3':
    f.close()