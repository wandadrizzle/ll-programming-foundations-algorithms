#Sets can only contain unique values - a dictionary can be used a set
print("Set:")
# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# create a set to perform a filter
unique_items = set()

# loop over each item and add to the set
for item in items:
    unique_items.add(item)
print(unique_items)

# Count the unique letters in a sentence
sentence = "The quick brown fox jumps over the lazy dog."
unique_items = {c for c in sentence.lower() if c.isalnum()}
print(unique_items)

print("\nDictionary:")
# create a hashtable object to hold the items and counts
#counter = dict()
counter = {}

# iterate over each item and increment the count for each one
for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

# print the results
print(counter)

print("\nFind max with recursion:")
# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(items):
    # breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]

    # otherwise get the first item and call function
    # again to operate on the rest of the list
    val1 = items[0]
    val2 = find_max(items[1:])
    print(val1, val2)

    # perform the comparison when we're down to just two
    if val1 > val2:
        return val1
    else:
        return val2


# test the function
print(find_max(items))