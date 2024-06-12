import random
while True:
    choices = ["Rock", "Paper", "Scissors"]

    #.choices() = show as the same type of arguments
    #.choice() = show as str
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('Rock, Paper or Scissors?: ').capitalize()
        if player == computer:
            print("Ops: ",computer)
            print("Me: ",player)
            print('Tie!')
        elif player == 'Rock':
            if computer == 'Paper':
                print("Ops: ",computer)
                print("Me: ",player)
                print('You lose!')
            if computer == 'Scissors':
                print("Ops: ",computer)
                print("Me: ",player)
                print('You win!')
        elif player == 'Paper':
            if computer == 'Scissors':
                print("Ops: ",computer)
                print("Me: ",player)
                print('You lose!')
            if computer == 'Rock':
                print("Ops: ",computer)
                print("Me: ",player)
                print('You win!')
        elif player == 'Scissors':
            if computer == 'Rock':
                print("Ops: ",computer)
                print("Me: ",player)
                print('You lose!')
            if computer == 'Paper':
                print("Ops: ",computer)
                print("Me: ",player)
                print('You win!')
        
    play_again = input("Wanna play again? (Yes/No): ").capitalize()

    if play_again != 'Yes':
        break

print('Bye!')


