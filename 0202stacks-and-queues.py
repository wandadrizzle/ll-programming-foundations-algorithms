from collections import deque #This is pronounced deck

# TODO: create a new empty stack

stack = []
# TODO: push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# TODO: print the stack contents
print(stack)

# TODO: pop an item off the stack
print("\nAfter popping 2 items off:")
print("Let's peek before we pop",stack[-1]) 
stack.pop()
print("Let's peek before we pop",stack[-1]) 
stack.pop()
print(stack)
print("\nAfter inserting and pushing items in:")
stack.insert(1,36)
stack.append(72)
print(stack)

# TODO: create a new empty deque object that will function as a queue

queue = deque()
# TODO: add some items to the queue

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# TODO: print the queue contents
print("\nWorking with queues:")
print(queue)
# TODO: pop an item off the front of the queue

x = queue.popleft()
print(queue)
y = queue.pop()
print(queue)