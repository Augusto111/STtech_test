import os
import subprocess
import sys

'''
Used to excute the file which is judged as an executable file in the target path.

@param {string} path - the full target file path include the filename.
'''
def execu(path):
    result = os.system(path)
    #print(result)

'''
Used to get all of the files in the target directory recursively, and order them, 
then send each of them to judge whether they are executable file.

@param {string} path - the target file path not include the filename.
'''
def readFile(path):
    if not os.path.isdir(path):
        print("It's not a directory or not exist.")
        return
    elif not os.listdir(path):
        print("Empty directory")
        return
    else:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                judgeFilename(os.path.join(dirpath, filename))


'''
Used to judge the executable file. Used the method of pipe, redefine the output stream, put the result
from the terminal into the buffer memory. Then analysis the result, if the string has 'x', then it can be
executed.

@param {string} path - the full target file path include the filename.
'''
def judgeFilename(path):
    if(os.access(path, os.X_OK)):
        print("Now executing the file: " + path)
        execu(path)
        print('\n')


'''
Main function, input the target directory path.
'''
if __name__ == "__main__":
    path = sys.argv[1]
    #path = "./targetDir"
    readFile(path)




