import sys

def countdown(x):
    if x == 0:
        print("Done! :)") #This is my breaking condition
        #sys.exit()
        return #This might be better in larger code bases, flow will got to something after the function call
    else:
        print(x, "...")
        countdown(x-1)
        print("Hey!") #This is shown at the end when stack is unwound

countdown(5)
print("What?")