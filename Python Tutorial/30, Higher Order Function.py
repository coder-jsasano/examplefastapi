#Higher Order Function = a function that either:
#                        1, accepts a function as an argument
#                        2, returns a function
#                         (In python, functions are treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

#Higher Order func
def hello(func):
    text = func("Hello")
    print(text)

#how you call high order func
#hello(loud)
#hello(quiet)

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))


