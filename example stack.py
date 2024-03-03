class Stack:
    def __init__(self):
        self.items = []


    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0,item)


    def pop(self):
        if self.isEmpty!=0:
            return self.items.pop()
        else:
            print("Stack is empty")

    def peekStack(self):
        if self.isEmpty!=0:
            return self.items[len(self.items)-1]
        else:
            print("Stack is empty")

    def sizeStack(self):
        return len(self.items)





stack = Stack()

print(stack.isEmpty())

stack.push(1)
stack.push(5)
stack.push(7)
stack.push(9)

print(stack.items)


print(stack.pop())
print(stack.sizeStack())