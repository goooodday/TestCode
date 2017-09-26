#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import time
import json

# Running Status Report
RUN_Status = {
    'JobName': 'Filelist',
    'MaxCount': 0,
    'FileIndex': 0,
    'FileName': ''
}

def main(msg, buff=None):
    sub_files = os.listdir(msg['img_path'])
    files = len(sub_files)

    RUN_Status['MaxCount'] = files

    for idx, filename in enumerate(sub_files):
        RUN_Status['FileIndex'] = idx
        RUN_Status['FileName'] = filename

        if (buff == None):
            print ("%d %s" % (idx, filename))

        if (buff != None):
            data = buff.put(RUN_Status)
        time.sleep(0.01)
    print ('Total Files : ', files)

# Main Startup....
# *****************************************************************************

if __name__ == '__main__':
    # Command Param
    COMMAND_Param = {
        'command': "IMG_CONV",
        'img_path': '/ImageStorage/Original',
        'arg1': [100, 200, 300, 400, 500, 600, 700, 800, 101, 102, 103, 104, 105, 106, 107, 108],
        'arg2': ['A123B124']
    }

    main(COMMAND_Param)
