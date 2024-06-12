#Error and Exceptions

#a = 5  print(a) #SyntaxError
#a = 5 +'10' #TypeError
#a = 5/0  #ZeroDivisionError

#import somemodule #ModuleNotFoundError

#a = 5   #NameError
#b = c 

#f = open('somefile.txt') #FileNotFoundError

#a = [1,2,3]  
#a.remove(4)  #ValueError
#print(a)

#a = [1,2,3]  
#a[4]          #IndexError
#print(a)

#my_dict = {"name": "Jquan"}
#my_dict ["age"]              #KeyError

#x = -5
#if x < 0:
#    assert(x>=0), "x is not positive"  #AssertionError

#Exception
#x = -5
#if x < 0:
#    assert(x>=0)
    #raise Exception("x should be negative")

#try:
#    a = 5/1
#    b = a + 4
#except Exception as e:
#    print(e)
#except ZeroDivisionError as e:
#    print(e)
#except TypeError as e:
#    print(e)
#else:
#    print("Everything has no problem")
#finally:
#    print('cleaning up...')

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)
    
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)


