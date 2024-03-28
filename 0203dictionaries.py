# TODO: create a dictionary all at once

items = dict({"key1" : 1, "key2" : 2, "key3" : 3})
print(items)
# TODO: create a dictionary progressively, since they can grow and change

items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)
# TODO: replace an item
items2["key2"] = "two"
print(items2)

# TODO: try to access a nonexistent key
#print(items["key6"]) #ERROR

# TODO: iterate the keys and values in the dictionary
print("Key: \t Value:")
for key,value in items2.items():
    print(key,"\t",value)