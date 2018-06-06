from multiprocessing import Process
import random
import time
import multiprocessing

def produce(name,q):
    while True:
        for i in range(5):
            item = random.randint(1,5)
            q.put(item)
            print("生产者",name,"生产了",str(item))

def consume(name,q):
    while True:
        for i in range(5):
            item = q.get()
            print("消费者",name,"消费了",item)
if __name__ == '__main__':
    q =  multiprocessing.Queue(maxsize = 5)
    Process(target=produce, args=(1,q)).start()
    Process(target=consume, args=(2,q)).start()
