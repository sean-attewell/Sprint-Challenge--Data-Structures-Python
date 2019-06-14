class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # if self.current == self.capacity:
        #     self.current = 0
        #     self.storage[self.current] = item
        #     self.current += 1
        # else:
        #     self.storage[self.current] = item
        #     self.current += 1

        if self.current == self.capacity:
            self.current = 0

        self.storage[self.current] = item
        self.current += 1

    def get(self):
        storage_copy = self.storage[:]
        for i in range(0, len(storage_copy)):
            if storage_copy[i] == None:
                del storage_copy[i]
        return storage_copy


# test = RingBuffer(5)

# print(test.storage)
# test.append("one")
# test.append("two")
# print(test.storage)
# test.append("three")
# test.append("four")
# print(test.storage)

# print(test.get())
