#!/bin/bash

number=$1

for FILE in Split/test$number/*
do
  #echo $FILE
  #FILE=$(echo $FILE)
  #echo $FILE
  bash Questionable.sh $FILE &
done
