# stack implementation in python

# creating a stack
def creating_stack():
    stack = []
    return stack

# creating an empty stack
def s_empty(stack):
    return len(stack) == 0

# adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)

# removing an element from the stack
def pop(stack):
    if (s_empty(stack)):
        return "stack is empty"

    return stack.pop()

stack = creating_stack()
push(stack, str(1))
push(stack, str(4))
push(stack, str(5))
push(stack, str(6))
push(stack, str(2))
print("pop item: " + pop(stack))
print("stack after poping an element: " + str(stack))
