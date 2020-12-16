
class ArrayQueue:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self,item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        item = self._data[0]
        self._data = self._data[1:]
        return item

    def first(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]

    def debug(self):
        return self._data


customQueue = ArrayQueue()
customQueue.enqueue(45)
customQueue.enqueue(46)
customQueue.enqueue(43)
print(customQueue.debug())
print(customQueue.first())
print(f"{customQueue.dequeue()} data is dequeued")
print(f"{customQueue.dequeue()} data is dequeued")
print(customQueue.debug())
