import Queue
from threading import Thread

import DL_ImageGen as dgen

# Lunching Task
#********************************************
def TaskLuncher(msg, out_q):
    dgen.DirFileCount(msg, out_q)
    out_q.put("Done")

    print "Task Stop~~~~~~"

# Receive Task Result
#********************************************
def TaskReceiver(in_q):
    while True:
        # Get some data
        data = in_q.get()
        if (data == "Done"):
           break

        print data
        in_q.task_done()

    print "Task Finished~~~~"

# Create MultiTaskManager
#*******************************************
def MultiTaskManager(msg):
    q = Queue.Queue()
    t1 = Thread(target=TaskReceiver, args=(q,))
    t2 = Thread(target=TaskLuncher, args=(msg, q,))
    t1.start()
    t2.start()
    q.join()


if __name__ == "__main__":
    path_file = 'D:/SubDirectoryFiles'
    MultiTaskManager(path_file)
