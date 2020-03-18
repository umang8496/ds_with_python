# Array based Queue Implementation

class Queue(object):
    def __init__(self,capacity):
        self.size = 0
        self.front = -1
        self.rear = -1
        self.queue = [None]*capacity
        self.capacity = capacity
    ##END

    def isQueueEmpty(self):
        return self.size == 0
    ## END

    def isQueueFull(self):
        return self.size == self.capacity
    ## END

    def enQueue(self,value):
        if self.isQueueEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = value
            self.size += 1
            print(value, "enQueued")
        elif self.isQueueFull():
            print("Queue is Full")
            return
        else:
            self.rear += 1
            self.queue[self.rear] = value
            self.size += 1
            print(value, "enQueued")
        ## END
    ## END

    def deQueue(self):
        if self.isQueueEmpty():
            print("Queue is Empty")
            return
        else:
            removed_value = self.queue[self.front]
            print()
            print(removed_value, "dequeued")
            self.front += 1
            self.size -= 1
            if (self.front > self.rear):
                self.front = self.rear = -1
            ## END
        ## END
    ## END

    def printQueue(self):
        print("Queue Elements",self.front,":", self.rear)
        for i in range(self.front,self.rear+1):
            print(self.queue[i], end=' ', flush=False)
        ## END
        print()
    ## END

    def getSizeOfQueue(self):
        return self.size
    ## END

    def deleteQueue(self):
        del self.queue
    ## END

    def frontOfTheQueue(self):
        print("front of the queue :", self.queue[self.front])
    ## END
## END    


if __name__ == "__main__":
    q1 = Queue(10)  # capacity is of 10 elements
    # print("Is the Queue Full ?", q1.isQueueFull())
    # print("Is the Queue Empty ?", q1.isQueueEmpty())

    q1.enQueue(10)
    q1.enQueue(20)
    q1.frontOfTheQueue()
    q1.enQueue(30)
    q1.enQueue(40)
    q1.frontOfTheQueue()
    q1.printQueue()
    q1.deQueue()
    q1.frontOfTheQueue()
    q1.enQueue(50)
    q1.printQueue()
## END



# This is the CircularQueue class
# class CircularQueue:
# 	def __init__(self, maxSize):
#     	self.queue = list()
# 	    self.maxSize = maxSize
# 	    self.head = 0
# 	    self.tail = 0

# 	def enqueue(self, data):
#     	if self.size() == (self.maxSize - 1):
#       		return("Queue is full!")
#     	else:
#       		self.queue.append(data)
#       		self.tail = (self.tail+1) % self.maxSize
#       		return True

#     def dequeue(self):
#     	if self.size() == 0:
#       		return("Queue is empty!")
#     	else:
#       		data = self.queue[self.head]
#       		self.head = (self.head+1) % self.maxSize
#       		return data
  
# 	def size(self):
#     	if self.tail >= self.head:
#       		qSize = self.tail - self.head
#     	else:
#       		qSize = self.maxSize - (self.head - self.tail)
#     	return qSize

# # input 7 for the size or anything else
# size = input("Enter the size of the Circular Queue")
# q = CircularQueue(int(size))

# print(q.enqueue(10))
# print(q.enqueue(20))
# print(q.enqueue(30))
# print(q.enqueue(40))
# print(q.enqueue(50))
# print(q.enqueue('Studytonight'))
# print(q.enqueue(70))
# print(q.enqueue(80))
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())


