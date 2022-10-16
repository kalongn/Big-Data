#/bin/bash

for i in {00..26};do
  cd test$i
  #rm content******.txt
  split -l 630 -d --additional-suffix=.txt file$i.txt content
  cd ../
done
