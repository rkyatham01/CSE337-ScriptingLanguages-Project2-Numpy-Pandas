# Run this script from the repository's root.
import re
import os

def rename(path):
    regexString = '^snap\d{3}.txt$'
    objectRet = re.compile(regexString)
    
    arr = list(filter(objectRet.match, os.listdir(path)))
    minimum = int(min(arr)[4:7])
    c = minimum
    
    for files in arr:
        if int(files[4:7]) == c:
            c += 1
            continue
        else:
            os.rename(os.path.join(path, files),os.path.join(path, f'snap{int(c):03d}.txt'))
        c += 1
    
    return True
