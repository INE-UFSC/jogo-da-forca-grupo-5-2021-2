import random
from words import fruits, animals, objects, colors, soccer_teams, random_list
from time import sleep

tested = []
count = 0
end_count = 0
again = True


def validate_input(guessed, word):
    global count
    global tested
    if len(guessed) != 1:
        print('Entrada invalida! Digite apenas uma letra por vez')
        guess()
    elif guessed not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print('Entrada invalida! Digite uma letra')
        guess()

    elif guessed in tested:
        print('Entrada invalida! Você já digitou essa letra...')
        guess()
    else:
        tested.append(guessed)
        if guessed not in word:
            print(f'\nA letra {guessed} não está na palavra!')
            count += 1
        hangman()
        validate_guess(word)
        print(f"Letras testadas: {tested}")
        print(f'Vidas: {6 - count}')


def validate_guess(word):
    global end_count
    end_count = 0
    for l in word:
        if l in tested:
            print(l, end=' ')
            end_count += 1
        else:
            print('_ ', end=' ')
    print()
    print()


def hangman():
    global count
    print("\n _____")
    print("|     |")

    if (count == 0):
        print("|     ")
        print("|     ")
        print("|     ")

    elif (count == 1):
        print("|     O")
        print("|     ")
        print("|     ")

    elif (count == 2):
        print("|     O")
        print("|     |")
        print("|     ")

    elif (count == 3):
        print("|     O")
        print("|    /|")
        print("|     ")

    elif (count == 4):
        print("|     O")
        print("|    /|\ ")
        print("|     ")

    elif (count == 5):
        print("|     O")
        print("|    /|\ ")
        print("|    / ")

    elif (count == 6):
        print("|     O")
        print("|    /|\ ")
        print("|    / \ ")

    print('|\n|__')
    print()
