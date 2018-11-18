import os
import subprocess

'''
Used to excute the file which is judged as an executable file in the target path.

@param {string} path - the full target file path include the filename.
'''
def execu(path):
    result = os.system(path)
    print(result)

'''
Used to get all of the files in the target folder, and order them, 
then send each of them to judge whether they are executable file.

@param {string} path - the target file path not include the filename.
'''
def readFile(path):
    pathList = os.listdir(path)
    pathList.sort()
    for filename in pathList:
        #execu(os.path.join(path, filename))
        judgeFilename(os.path.join(path, filename))

'''
Used to judge the executable file. Used the method of pipe, redefine the output stream, put the result
from the terminal into the buffer memory. Then analysis the result, if the string has 'x', then it can be
executed.

@param {string} name - the full target file path include the filename.
'''
def judgeFilename(name):
    showFile = subprocess.Popen(["ls", "-l",name], stdout=subprocess.PIPE)
    filePermission = (str(showFile.stdout.read())).split(" ")[0]
    #print(filePermission)
    if(filePermission.find("x")):
        print("Now executing the file: " + name)
        execu(name)
        print('\n')

'''
Main function, input the target folder path.
'''
if __name__ == "__main__":
    path = input("Please input your target folder path:")
    #path = "./target"
    readFile(path)




