import os

def execu(main):

    #main = ".\\gedit\\1.exe"

    r_v = os.system(main)

    print(r_v)

def readFile(path):

    path_list = os.listdir(path)

    path_list.sort()  # 对读取的路径进行排序

    for filename in path_list:
        execu(os.path.join(path, filename))

if __name__ == "__main__":
    path = ".\\gedit"
    readFile(path)




