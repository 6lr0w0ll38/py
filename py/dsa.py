#queue implementation in Python

class queue:

    #creating queue
    def __init__(self):
        self.queue = []

    #add an element
    def enqueue(self, item):
        self.queue.append(item)

    #remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    #print  the queue
    def print(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

#driver code
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.print()

q.dequeue()

print('After removing an element')
q.print()
