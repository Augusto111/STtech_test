#!/bin/bash

function getDir(){
    for element in `ls $1`
    do  
        dirOrFile=$1"/"$element
        #judge exist or not
        if [ -d $dirOrFile ]
        then 
            getDir $dirOrFile
        else
        	#judge can be excuted or not
        	if [ -x $dirOrFile ]
        	then
        		echo "Now executing the file: "$dirOrFile
            	$dirOrFile
            	echo -e '\r'
            fi
        fi  
    done
}
#myPath="./targetDir"
getDir $1