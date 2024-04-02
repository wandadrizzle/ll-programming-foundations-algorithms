items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

reverse1 = items1[::-1]
print("Descending items 1",reverse1)

items3 = [87, 56, 53, 49, 41, 23, 20, 19, 8, 6]
items4 = [53, 49, 41, 87, 23, 56, 19, 8, 20, 6]

def is_sorted(itemlist):
    # using the all function
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

    # using the brute force method
    # for i in range(0, len(itemlist)-1):
    #     if (itemlist[i] > itemlist[i+1]):
    #         return False
    # return True

print(is_sorted(items1))
print(is_sorted(items2))

def is_sorted_wanda(itemlist):
    if itemlist[0] < itemlist[1]: #ascending
        for i in range(0, len(itemlist) -1):
             if (itemlist[i] > itemlist[i+1]):
                return False
        return True
    if itemlist[0] > itemlist[1]: #descending
        for i in range(0, len(itemlist) -1):
            if (itemlist[i] < itemlist[i+1]):
                return False
        return True
    
print(is_sorted_wanda(items1))
print(is_sorted_wanda(items2))
print(is_sorted_wanda(items3))
print(is_sorted_wanda(items4))