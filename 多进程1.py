from multiprocessing import Process
import random
import time
import multiprocessing

def produce(name,e,q):
    while True:
        for i in range(5):
            e.acquire()
            item = random.randint(1,5)
            q.send(item)
            print("生产者",name,"生产了",str(item))

def consume(name,e,q):
    while True:
        for i in range(5):
            item = q.recv()
            print("消费者",name,"消费了",item)
            e.release()
if __name__ == '__main__':
    parent_conn, child_conn  =  multiprocessing.Pipe()  
  
    e = multiprocessing.Semaphore(5)  
         
    Process(target=produce, args=(1,e,child_conn)).start()    
  
    Process(target=produce, args=(2,e,child_conn)).start() 
