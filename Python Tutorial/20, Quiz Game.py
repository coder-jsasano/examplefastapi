def new_game():
    
    guesses = []
    correct_guesses = 0
    question_no = 1

    for key in questions:
        print("----------------------------------")
        print(key)
        for i in options[question_no-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_no += 1
    print("----------------------------------")

    display_score(correct_guesses, guesses)



def check_answer(answer, guess):
    if answer == guess:
        print('Correct!')
        return 1
    else:
        print('Wrong!')
        return 0

def display_score(correct_guesses, guesses):
    print("----------------------------------")
    print('Results')
    print("----------------------------------")
    
    print("Answers: ",end='')
    for i in questions:
        print(questions.get(i), end=' ')
    print()

    print("Guesses: ",end='')
    for i in guesses:
        print(i, end=' ')
    print()

    score = int((correct_guesses/len(questions))*100)
    print('Your score is '+str(score)+ '%')

    

def play_again():
    response = input('Wanna continue? (Yes/No): ')
    response = response.capitalize()

    if response == 'Yes':
        return True
    else:
        return False
    


questions = {
    "The race of Kai Cenat?":"B",
    "Where is Ishowspeed from?":"B",
    "Who is Ishowspeed's most recent ex?":"C",
    "What did Ray say that scared Kai?": "A"
}

options = [["A. White", "B. Black", "C. Asian", "D. Latina"],
           ["A. LA", "B. Ohio", "C. Texas", "D. Florida"],
           ["A. Dream", "B. Ninon", "C. Alliah", "D. Adin"],
           ["A. Bitch ass ling-ling", "B. Bitch ass nword", "C. Bitch ass cunt", "D. Bitch ass shit"]]

new_game()

while play_again():
    new_game()

print('Bye!')

