# running a function in another thread
from time import sleep, ctime
from threading import Thread

#a custom funtion that blocks for a moment
def task ():
    #block for a moment
    sleep(1)
    #display a message
    print(f'{ctime()} This is from another thread')
          
#create a thread
thread = Thread(target=task)
#run thread
thread.start()
#wait for thread to finnish
print(f'{ctime()} Waiting for the trhead')
thread.join() 