import random

options = ('piedra', 'papel', 'tijera')
rondas = 1

computerWins=0
userWins=0

while True:

    print('*' * 10)
    print('Ronda ', [rondas])
    print('*' * 10)

    print('Computer wins = ', computerWins)
    print('User wins = ', userWins)
    user_option = input('Escriba: piedra, papel, tijera = ')
    user_option = user_option.lower()
    computer_option = random.choice(options)

    if user_option == 'piedra' or user_option == 'papel' or user_option == 'tijera':

        print('User=', userWins)
        print('Computer= ', computerWins)
        if user_option == computer_option:
            print("Empate")
        elif user_option == 'piedra':
            if computer_option == 'tijera':
                print('piedra gana a tijera')
                print('User ganó')
                userWins += 1
            else:
                print('Papel gana a Piedra')
                print('Computer ganó')
                computerWins += 1

        elif user_option == 'papel':
            if computer_option == 'piedra':
                print('papel gana a piedra')
                print('User ganó')
                userWins += 1
            else:
                print('tijera gana a papel')
                print('Computer ganó')
                computerWins += 1
        elif user_option == 'tijera':
            if computer_option == 'papel':
                print('tijera gana a papel')
                print('User ganó')
                userWins += 1
            else:
                print('Piedra gana a tijera')
                print('Computer ganó')
                computerWins += 1
    else:
        print("Valor ingresado con corresponde con la solicitud")
        continue

    if computerWins == 3:
        print('Despues de ', rondas, ' rondas el ganador fue Computer')
        print('Resultado:')
        print('User=', userWins)
        print('Computer= ', computerWins)
        break
    elif userWins == 3:
        print('Despues de ', rondas, ' rondas el ganador fue User')
        print('Resultado:')
        print('User=', userWins)
        print('Computer= ', computerWins)
        break
    rondas += 1




