#!/usr/bin/python

from pathlib import Path
from shutil import copyfile
import sys

extensions_allowed = ['.jpg', '.png', '.jpeg', '.bmp', '.gif']

#------------------------------------------------------------------------------

def enlist(path, list_dst):

    for file in path.iterdir():
        if file.is_file():
            ext = file.suffix
            if ext in extensions_allowed:
                list_dst.append(file)
        elif file.is_dir():
            enlist(file, list_dst)

#------------------------------------------------------------------------------
            
def copy_with_indexing(list_src, path_dst):

    if not path_dst.is_dir():
        print(path_dst, 'is not a directory!')
        return
    
    n = 1
    
    for file in list_src:
        dst = path_dst.as_posix() + '/' + str(n) + file.suffix
        copyfile(file.as_posix(), dst)
        n = n + 1

#------------------------------------------------------------------------------

arg_count = len(sys.argv)
if arg_count != 3:
    print('Usage: src_folder dst_folder')
    sys.exit()

path_1 = Path(sys.argv[1])
path_2 = Path(sys.argv[2])

list_src = []
enlist(path_1, list_src)
copy_with_indexing(list_src, path_2)