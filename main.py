import game

while True:
    game.word
    game.hangman()
    game.validate_guess(game.word)
    while (game.end_count < len(game.word)) and (game.count < 6):
        guess = game.guess()
    game.end_game_message()
