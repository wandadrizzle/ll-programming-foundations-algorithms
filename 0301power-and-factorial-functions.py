# Using recursion to implement power and factorial functions

# 2^4 = 2*2*2*2 = 16
def power(num, pwr):
    if pwr == 0:
        return 1
    elif pwr < 0 or not isinstance(pwr, int): #Have to do it this way since this is a recursion chapter!
        print("This function only works for +ve integers")
    else:
        return (num * power(num, pwr-1)) #pwr aacts as count?
        #return num ** pwr #no recursion?



# 5! = 5*4*3*2*1
# Special case: 0! is 1, because... math
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(f"5 to the power of 3 is {power(5, 3)}")
print(f"2 to the power of 4 is {power(2, 4)}")
print(f"4! is {factorial(4)}")
print(f"0! is {factorial(0)}")
print(f"1! is {factorial(1)}")