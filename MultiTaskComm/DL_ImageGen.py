#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import json

RUN_Status = {
    'MaxCount': 10,
    'CurrentCount': 1,
    'FileName': ''
}


def DirFileCount(msg, buff):
    path_name = msg['file_path']
    tot_files = 0

    for dir_path in os.listdir(path_name):
        sub_dir = path_name + '/' + dir_path

        sub_files = os.listdir(sub_dir)

        files = len(sub_files)

        RUN_Status['MaxCount'] = files

        cnt = 0;
        for file in sub_files:
            cnt = cnt + 1
            RUN_Status['CurrentCount'] = cnt
            RUN_Status['FileName'] = file
            data = buff.put(RUN_Status)
            time.sleep(0.01)

        tot_files = tot_files + files
        #print dir_path, ' - ', files

    #print 'Total Files : ', tot_files

# Main Startup....
# *****************************************************************************

if __name__ == '__main__':
    DirFileCount('D:/SubDirectoryFiles')
