x = "awesome"

def myFunc():
    print ("Python is " + x)

myFunc()

#If you create a variable with the same name inside a function, this variable will be local, 
# and can only be used inside the function. 
#The global variable with the same name will remain as it was, global and with the original value.

def myFunc2():
    x = "fantastic"
    print ("Python is " + x)

myFunc2()

print ("Python is " + x)


#To create a global variable inside a function, you can use the global keyword.
def myFunc3():
    global x
    x = "fantastic"

myFunc3()

print ("Python is " + x)