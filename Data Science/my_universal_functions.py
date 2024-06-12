def checkIfNotNumeric(**args):
    retValue = True
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True

def checkIfNotNumeric2(L):
    retValue = True
    for x in L:
        if not(isinstance(x,(int,float))):
            return False
    return True

def addAllNumerics(*args):
    s = 0
    for x in args:
        s += x
    return s

myName = 'Python Course'


