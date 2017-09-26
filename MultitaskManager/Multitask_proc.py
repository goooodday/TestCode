#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import queue
from threading import Thread
import json

from ImageGen import main as ImgGen


# Lunching Task
#********************************************
def TaskLuncher(msg, out_q):

    if (msg['command'] == "IMG_CONV"):
        ImgGen(msg, out_q)

    elif (msg['command'] == "TRAIN_TASK"):
        pass

    elif (msg['command'] == "RECOGNITION_TASK"):
        pass

    out_q.put("Done")
    print ("Task Stop~~~~~~")

# Receive Task Result
#********************************************
def TaskReceiver(in_q):
    while True:
        # Get some data
        data = in_q.get()
        if (data == "Done"):
           break

        if (data['JobName'] == 'Filelist') :
            print (data['MaxCount'] , data['FileIndex'], data['FileName'])

        in_q.task_done()

    print ("Task Finished~~~~")

# Create TaskRunner
#*******************************************
def TaskRunner(msg):
    q = queue.Queue()
    t1 = Thread(target=TaskReceiver, args=(q,))
    t2 = Thread(target=TaskLuncher, args=(msg, q,))
    t1.start()
    t2.start()
    q.join()


def readConfig(filename) :
    f = open(filename, 'r')
    js = json.loads(f.read())
    f.close()
    return js

def writeConfig(filename, str) :
    f = open(filename, 'w')
    f.write (json.dumps(str))
    f.close()

if __name__ == "__main__":

    # Command Param
    COMMAND_Param = {
        'command': "IMG_CONV",
        'img_path': '/ImageStorage/Original',
        'arg1': [100, 200, 300, 400, 500, 600, 700, 800, 101, 102, 103, 104, 105, 106, 107, 108],
        'arg2': ['A123B124']
    }

    # Write JSON File from COMMAND_Param
    writeConfig("test.json", COMMAND_Param)

    # Single Runner
    # *************************
    TaskRunner(COMMAND_Param)

    # Define Multi Runner
    # *************************
    tm1 = Thread(target=TaskRunner, args=(COMMAND_Param,))
    #tm2 = Thread(target=TaskRunner, args=(COMMAND_Param,))

    # Start Multi Runner
    #*************************
    tm1.start()
    #tm2.start()

    print ("Main Task Stop")
