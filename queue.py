class Queue(object):

    def __init__(self):
        self.queue = []

    def dequeue(self):
        return self.queue.pop(0)

    def enqueue(self, element):
        self.queue.append(element)

    def size(self):
        return len(self.queue)
#hello
    def isEmpty(self):
        return len(self.queue) == 0

    def __iter__(self):
        for item in self.queue:
            yield item
