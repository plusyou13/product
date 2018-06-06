def consumer():
    print('启动生成器\n') # 只有第一次会执行(启动生成器), 之后再调用生成器就会从yield处执行
    while True:
        n = yield # Python的yield不但可以返回一个值，它还可以接收调用者发出的参数
        print('接受到产品%s...'%n) 
        print('消费产品 %s...\n' % n)

def produce(c):
    #c.send(None)
    next(c)
    #通过c.send(None)或者next(c)启动生成器函数，并执行到第一个yield语句结束的位置
    print('开始生产产品...')
    n = 0
    while n < 5:
        n = n + 1
        print('生成产品 %s...' % n)
        print('打包发送产品 %s...' % n)
        r = c.send(n) # # 获取生成器consumer中由yield语句返回的下一个值
        
    c.close()
    
if __name__ == '__main__':
    c = consumer()   #创建生成器
    print('创建生成器')
    produce(c)
