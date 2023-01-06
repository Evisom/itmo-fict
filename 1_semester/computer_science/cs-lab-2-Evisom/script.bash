#!/bin/bash
x=$1
y=$2

let sum=$x+$y
let dif=$x-$y
let pr=$x*$y

if [[ $y -eq 0 ]]
then
    div="#"
else
    div=$(bc<<<"scale=2;$x/$y")
    if [[ $x/$y -eq 0 ]]
    then
        if [[ ${div:0:1} == "-" ]]
        then
            div="-0"${div:1}
        elif [[ $div == "0" ]]
        then
            div="0.00"
        else
            div="0"$div
        fi
    fi 
fi

echo $sum $dif $pr $div