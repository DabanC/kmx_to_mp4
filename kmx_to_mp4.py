#!/usr/bin/env python3

import os.path as path
import getopt
import sys

BUFFER_SIZE = 200
SEEK = 34

def kmx_to_mp4(file_path):
    if not path.exists(file_path):
        print('文件不存在！！！')
        sys.exit(2)
    file_name, file_type = path.splitext(path.basename(file_path))
    file_dir = path.dirname(file_path)
    file_size = path.getsize(file_path)
    if file_type != '.kmx':
        print('似乎不是一个kmx文件！')
        sys.exit(2)
    out_path = path.join(file_dir, file_name + '.mp4')
    print(file_name)
    with open(file_path, 'rb') as f:
        f.seek(SEEK)
        out_file = open(out_path, 'wb')
        while True:
            buffer = f.read(BUFFER_SIZE)
            if (len(buffer) > 0):
                out_file.write(buffer)
                out_file_size = path.getsize(out_path)
                print('已完成{0}%'.format(round(out_file_size/file_size * 100, 2)), end='\r')
            else:
                print("转换完成！！！")
                f.close()
                out_file.close()
                break

def get_path(argv):
    file_path = ''
    try:
        opts,args = getopt.getopt(argv, "hi:", ["infile="])
        if len(opts) == 0:
            raise getopt.GetoptError('没有参数')
    except getopt.GetoptError:
        print('kmx_to_mp4 -i <filename>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('kmx_to_mp4 -i <filename>')
        elif opt in ('-i', '--infile'):
            file_path = arg
    return file_path
if __name__ == '__main__':
    file_path = get_path(sys.argv[1:])
    kmx_to_mp4(file_path)