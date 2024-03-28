print("The Bubble Sort:")

array = [23, 8, 15, 17, 4, 40, 11, 31]
length = len(array)

def bubbleSort(dataset):
    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
        print("Current State:", dataset)       

print("This is the original list: ", end="")
for i in range(length):
    print(array[i], end=" ")
print("\n")

bubbleSort(array)
print("Result?", array)

print("\nThe Bubble Sort:") #Better performance


