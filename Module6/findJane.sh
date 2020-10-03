#!/bin/bash
> oldFiles.txt
files=`grep " jane " ../data/list.txt | cut -d' ' -f 3`
for file in $files
do
        if test -e "/home/student-01-a444a1faf525$file";
        then
                echo "/home/student-01-a444a1faf525$file" >> oldFiles.txt
        fi
done
