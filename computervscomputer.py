import random

lista = ['rock','paper','scissors']

while True:
  try:
    i = random.randint(0,100)
    j = random.randint(0,100)
    pick1 = i%3
    pick2 = j%3
    wins = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }

    print 'Computer1 picked %s and computer2 chose %s' % (lista[pick1], lista[pick2])

    if wins[lista[pick1]] == lista[pick2]:
        print 'Computer 2 won!'
    elif lista[pick1] == lista[pick2]:
        print 'Draw!'
    else:
        print 'Computer 1 won!'
    k = raw_input('Idz dalej ')
  except KeyboardInterrupt:
    pass
