#!/bin/bash

success=0
fail=0

function getDir(){
    a=1
    for element in `find $1 -name '*'`
    do
        if [ $1 = $element ]||[ -d $element ]
        then
               continue
        else
            a=0
            #judge can be excuted or not
            if [ -x $element ]
            then
                echo "Now executing the file: "$element
                $element
                if [ $? = 0 ]
                then
                    ((success++))
                else
                    ((fail++))
                fi
                echo -e '\r'
            fi
        fi
    done

    return $a
}
#myPath="./targetDir"
if [ "$1" = "" ]
then
    echo "Error: Missing directory parameters.You can input:
  './execution_exe.sh -h'
to get help."
    exit 3
else
    if [ "$1" = "-h" ]||[ "$1" = "--help" ]
    then
        echo "usage: ./execution_exe.sh [the target directory path]
[your target directory path]: it's the absolute path or relative path in the file system.
-h: print this help message and exit (also --help)
Exit:
0: Success
1: Target directory is empty
2: Target directory is not existed
3: Missing directory parameters
"
    else
        if [ -d $1 ];then
            getDir $1
            if [ $? -eq 0 ]
            then
                echo "Success."
                echo $success" succeeded, "$fail" failed."
                exit 0
            else
                if [ $? -eq 1 ]
                then
                    echo "Warning: target directory is empty"
                    exit 1
                fi
            fi
            #echo "$a"
        else
            echo "Error: Nonexistent directory. Please check the target directory."
            exit 2
        fi
    fi
fi

