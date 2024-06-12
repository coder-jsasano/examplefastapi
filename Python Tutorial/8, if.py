#if statement

#age = int(input('How old are ya?: '))

#if age == 100:
#    print('You are a century old!')
#elif age >= 20:
#    print('You are an adult!')
#elif age < 0:
#    print("You haven't been borned yet")
#else:
#    print('You are a child!')
#--------------------------------------------------------------------------------------------------------
temp = int(input("What is the temperature outside?: "))

#if temp >= 0 and temp <= 30:
#    print('The temperature is good today!')
#    print('Go touch some glass!')
#elif temp < 0 or temp > 30:
#    print('The temperature is bad today!')
#    print('Stay inside!')

if not (temp < 0 or temp > 30):
    print('The temperature is good today!')
    print('Go touch some glass!')
elif not (temp >= 0 and temp <= 30):
    print('The temperature is bad today!')
    print('Stay inside!')





