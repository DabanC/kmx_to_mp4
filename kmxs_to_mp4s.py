#!/usr/bin/env python3

import os.path as path
import os
import sys
import getopt
import kmx_to_mp4

def kmxs_to_mp4s(file_dir):
    if path.exists(file_dir) and path.isdir(file_dir):
        file_name_list = os.listdir(file_dir)
        for file_name in file_name_list:
            if not file_name.endswith('.kmx'):
                continue
            file_path = path.join(file_dir, file_name)
            kmx_to_mp4.kmx_to_mp4(file_path)



def get_path(argv):
    file_path = ''
    try:
        opts,args = getopt.getopt(argv, "hi:", ["infile="])
        if len(opts) == 0:
            raise getopt.GetoptError('没有参数')
    except getopt.GetoptError:
        print('kmx_to_mp4 -i <filedir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('kmx_to_mp4 -i <filedir>')
        elif opt in ('-i', '--infile'):
            file_path = arg
    return file_path

if __name__ == '__main__':
    file_path = get_path(sys.argv[1:])
    kmxs_to_mp4s(file_path)