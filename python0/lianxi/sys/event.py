
import multiprocessing
import time

def waif_for_event(e):
    '''Waiting for the event to set befor doing anything'''
    print 'waif_for_event : starting'
    e.wait()
    print 'wait_for_event:e.is_set()->',e.is_set()

def wait_for_event_timeout(e,t):
    '''wait seconds and then timeout'''
    print 'wait_for_event_timeout : starting'
    e.wait(t)
    print 'wait_for_event_timeout : e.is_set()->',e.is_set()

if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name = 'black',target = wait_for_event,args = (e,))

    w1.start()

    w2 = multiprocessing.Process(name = 'non-block',target = wait_for_event_timeout,args = (e,2))
    
