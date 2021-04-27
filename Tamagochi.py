# TAMAGOCHI 

# CREATED BY DANDY 


user = input('USERNAME: ')
age = input('AGE: ')

player = {'USERNAME: ':user, 'AGE: ':age, 'Power':100}
enemies = {'NAME: ':'Jojo', 'Power':250}

print('\nHello', user)
def startgame():
    choice = input('\nCHOOSE: \n1.EAT \n2.CHECK STATUS \n3.CHECK ENEMIES \n4.ATTACK \n5.EXIT \n')
    if choice == "1":
        goEAT()
    elif choice =='2':
        goCheck()
    elif choice =='3':
        goCheckEnemies()
    elif choice =='4':
        goAttack()
    else:
        goExit()

def goEAT():
    print('NYAM.. NYAM.. NYAM..')
    player['Power'] += 100
    startgame()

def goCheck():
    print('CHECKING.. CHECKING.. CHECKING..')
    
    print(player)
    startgame()

def goCheckEnemies():
    print('SPYING.. SPYING.. SPYING..')
    print(enemies)
    startgame()

def goAttack():
    if player['Power'] > enemies['Power']:
        print('YOU WIN CONGRATULATIONS ', user)
        startgame()
    else:
        print('YOU LOSER!', user)
        goExit()
def goExit():
    print('Bye.. Bye..', user)

startgame()