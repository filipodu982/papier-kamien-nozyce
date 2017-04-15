import random

lista = ['rock','paper','scissors']
while True:
    player = raw_input('Pick a figure: ')
    if player not in lista:
        print 'Wrong figure!'
        pass
    else:
        break

i = random.randint(0,100)
pick = i%3
wins = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

print 'You chose %s and computer chose %s' % (player, lista[pick])

if wins[player] == lista[pick]:
    print 'You lost!'
elif player == lista[pick]:
    print 'Draw!'
else:
    print 'You won!'
