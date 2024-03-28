import math

array = [42, 69, 22, 28, 12]

print("The even elements: ")
#for i in range(int(len(array)/2)):
for i in range(math.ceil(len(array)/2)): # This rounds up :)
    print(array[2*i])

print("\nThe odd elements: ")
for i in range(len(array)):
    if(i == 0 or i % 2 == 0):
        continue
    else:
        print(array[i])