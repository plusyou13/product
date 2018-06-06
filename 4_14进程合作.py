from multiprocessing import Process,Semaphore
import time
def run(q,user):
    q.acquire()
    print('P'+str(user)+'开始' )
    time.sleep(3)
    print('P'+str(user)+'结束')
    q.release()
if __name__ == '__main__':
    q=Semaphore(1)
    p1=Process(target=run,args=(q,1))
    p1.start()
    q=Semaphore(3)
    p3=Process(target=run,args=(q,3))
    p4=Process(target=run,args=(q,4))
    p2=Process(target=run,args=(q,2))
    p5=Process(target=run,args=(q,5))
    p1.join()
    p3.start()
    p4.start()
    p2.start()
    p3.join()
    p4.join()
    p5.start()
    p2.join()
    p5.join()

