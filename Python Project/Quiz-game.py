print("Welcome to my calisthenics quiz!")

playing = input("Do you wanna play?: ")

if playing.lower() != "yes":
    quit()  #type TAB to make a proper indentation

print("Alright bet let's play!")
score = 0

answer = input("What does ROM stand for?: ")
if answer.lower() == "range of motion":
    print('Correct!')
    score += 1
else:
    print('Wrong:(')

answer = input("What does HSPU stand for?: ")
if answer.lower() == "hand stand push up":
    print('Correct!')
    score += 1
else:
    print('Wrong:(')

answer = input("What does MU stand for?: ")
if answer.lower() == "muscle up":
    print('Correct!')
    score += 1
else:
    print('Wrong:(')

answer = input("What does OAP stand for?: ")
correct_answers = ["one arm push up", "one arm pull up"]

if answer in correct_answers:
    print('Correct!')
    score += 1
else:
    print('Wrong:(')


percentage = (score / 4)*100
result = f"You got {score} questions correct!!\nThe rate is {percentage}%"

print(result)


