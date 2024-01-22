#!/usr/bin/bash
FILE=$1
while read NUMBERS;
do
    factors=($(factor $NUMBERS))
    first_factor=${factors[1]}
    echo "$NUMBERS=$(($NUMBERS/$first_factor))*$first_factor"
done < $FILE

