import random
sign = ['rock','paper','scissor']
systempt = 0
userpt = 0
n = int(input('how many matches you wanna play'))
for i in range(n):
    i = random.randint(0,2)
    computer = sign[i]
    user = input('Rock ... paper ... scissor...')
    print('computer:'+computer)
    if computer == user:
        print('Match tied')
    else:
         if computer == 'rock':
             if user == 'scissor':
                print('you lose!')
                systempt +=1
             elif user == 'paper':
                print('you win!!!')
                userpt +=1
         elif computer == 'paper':
            if user == 'rock':
                print('you lose!')
                systempt += 1
            elif user == 'scissor':
                print('you win!!')
                userpt+=1
         elif computer == 'scissor':
             if user == 'rock':
                print('YOu winn!!')
                userpt+=1
             elif user == 'paper':
                print('you lose!')
                systempt+=1
print('Systems point'+ str(systempt))
print('your point'+ str(userpt))
if systempt>userpt:
    print('winner of the match is system')
else:
    print('winner of the match is youuu!!')