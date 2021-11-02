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
        
def guess():
    guess = input("Adivinhe uma letra:").strip().upper()
    validate_input(guess, word)

def end_game_message():
    global word
    global end_count
    global count
    global tested
    if (end_count == len(word)):
        print(f'Jogador, você acertou a palavra secreta: {word}.\nParabéns, você venceu o jogo!\n')
    elif (count == 6):
        print(f'Jogador, você perdeu!\nA palavara correta era: {word}\n')
    tested = []
    count = 0
    end_count = 0
    menu()

def menu():

    print('Seja bem vindo jogador!')
    sleep(1)
    while True:
        menu = input(f'Por favor, escolha uma das classes de palavras para jogar:\n'
                    f'[1] - Frutas\n'
                    f'[2] - Animal\n'
                    f'[3] - Objeto\n'
                    f'[4] - Cor\n'
                    f'[5] - Time de Futebol\n'
                    f'[6] - Aleatorio (inclui todas as classes anteriores);\n'
                    f'[7] - Sair do Jogo.\n'
                     'Insira aqui: ')
        sleep(1)
        if menu == '1':
            word = random.choice(fruits)
            break
        elif menu == '2':
            word = random.choice(animals)
            break   
        elif menu == '3':
            word = random.choice(objects)
            break
        elif menu == '4':
            word = random.choice(colors)
            break 
        elif menu == '5':
            word = random.choice(soccer_teams)
            break
        elif menu == '6':
            word = random.choice(random_list)
            break
        elif menu == '7':
            quit()
        else:
            print('Por favor, selecione uma das opções válidas!')
    return word

word = menu()

def play_again():
    global word
    while True:
        play = input('Deseja continuar jogando? [sim/nao]\n'
            'Resposta: ')
        if play == 'sim' or 's':
            word = menu()
            break
        elif play == 'nao' or 'n':
            quit()
        else:
            print('Por favor, responda com "sim" ou "nao".')
        return again
        