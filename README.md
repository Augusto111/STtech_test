# STtech_test

This is a interview test of Sensetime. It will:
1. read all of the executable files from the gedit directory
2. execute these files according to alphabet order
3. if the executable file has the output, then print them to the terminal
4. we provide two method to achieve it: run python script or run shell script

## Usage
1. open the terminal
2. run :
    ```shell
    python execution_exe.py [your target directory path]
    ```
    or
    ```shell
    ./execution_exe.sh [your target directory path]
    ```
3. Both of the two script will return the exit code. 
If you want to call our script, you can judge it success 
or not by this
###   Note

1. The code relys on the python3, so please pay attention to the version of your python.
2. This code can only run on Linux.
3. You can use the "targetDir" to test like:
    ```shell
    python execution_exe.py ./targetDir
    ```
    or
    ```shell
    ./execution_exe.sh ./targetDir
    ```
4. You can use the command to get help:
    ```shell
    python execution_exe.py -h
    ```
    or
    ```shell
    ./execution_exe.sh -h
    ```
###   Exit Code:
* 0: Success
* 1: Target directory is empty
* 2: Target directory is not existed
* 3: Missing directory parameters
