
queue = list()

def enqueue(data):
    if data not in queue:
        queue.insert(0,data)
        return True
    return False

def dequeue():
    if len(queue)>0:
        return queue.pop()
    return ("Queue Empty!")

def size():
    return len(queue)
def printQueue():
    return queue

