import random

x = random.randint(1,6)
y = random.random() # show random number between 0 to 1

mylist = ['rock', 'paper', 'scissors']
z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)

#print(x)
#print(y)
#print(z)
print(cards)



