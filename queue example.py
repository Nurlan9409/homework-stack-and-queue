


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(5)
queue1.enqueue(6)
queue1.enqueue(7)
queue1.enqueue(8)
queue1.enqueue(9)
queue1.enqueue(10)

print(queue1.items)

print (queue1.size())

print(queue1.items.pop())
print(queue1.items)



