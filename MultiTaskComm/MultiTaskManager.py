import Queue
from threading import Thread
import json

import DL_ImageGen as dgen

# Lunching Task
#********************************************
def TaskLuncher(msg, out_q):
    if (msg['command'] == "DCONV"):
        dgen.main(msg, out_q)

    elif (msg['command'] == "DCTRN"):
        pass

    elif (msg['command'] == 'DCINF'):
        pass

    elif (msg['command'] == 'DCLUS'):
        pass
    
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

        print data['MaxCount'] , data['CurrentCount'], data['FileName']
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

# Read JSON Config File
#*******************************************
def readConfig(filename) :
    f = open(filename, 'r')
    js = json.loads(f.read())
    f.close()
    return js

# Write JSON Config File
#*******************************************
def writeConfig(filename, str) :
    f = open(filename, 'w')
    f.write (json.dumps(str))
    f.close()

if __name__ == "__main__":
    
    COMMAND_Param = {
        'command': "DCONV",
        'file_path': 'D:/SubDirectoryFiles'
    }
    
    # Write JSON File from COMMAND_Param
    writeConfig("test.json", COMMAND_Param)
    
    # Single Runner
    # *************************
    # MultiTaskManager(COMMAND_Param)

    # Define Multi Runner
    # *************************
    tm1 = Thread(target=MultiTaskManager, args=(COMMAND_Param,))
    #tm2 = Thread(target=MultiTaskManager, args=(COMMAND_Param,))

    # Start Multi Runner
    #*************************
    tm1.start()
    #tm2.start()

    print "Main Task Stop"
