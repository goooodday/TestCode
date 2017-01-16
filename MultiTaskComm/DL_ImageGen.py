#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

def DirFileCount(path_name, buff):

    tot_files = 0

    for dir_path in os.listdir(path_name):
        sub_dir = path_name + '/' + dir_path

        files = len(os.listdir(sub_dir))
        data = buff.put(tot_files)

        tot_files = tot_files + files
        print dir_path, ' - ', files

    print 'Total Files : ', tot_files

# Main Startup....
# *****************************************************************************

if __name__ == '__main__':
    DirFileCount('D:/SubDirectoryFiles')
