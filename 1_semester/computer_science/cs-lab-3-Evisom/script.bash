#!/bin/bash
export LANG=en_US.UTF-8

# 1 - path 

if [[ $1 == "" ]] # Check for empty input
then
    path=$(pwd)
    echo "."
else 
    path=$1
    echo $path
fi

dir_count=0
file_count=0

function tree () 
{
    # 1 - path 
    # 2 - branch 
    local subdirs=($1/*)

    for i in ${!subdirs[@]}
    do
        local parent=$'\u2502\u00A0\u00A0\u0020'
        local child=$'\u251c\u2500\u2500\u0020'
        local name=${subdirs[i]##*/}

        if [[ $i -eq $(( ${#subdirs[@]} - 1 )) ]] # Last file in directory
        then
            parent=$'\u0020\u0020\u0020\u0020'
            child=$'\u2514\u2500\u2500\u0020'
        fi

        echo "$2$child$name"

        if [[ -d $1/$name ]]
        then # Directory
            dir_count=$(( $dir_count + 1 ))
            tree $1/$name "$2$parent"
        else # File
            file_count=$(( $file_count + 1 ))
        fi
    done
}

tree $path

if [[ $dir_count -eq 1 ]] # Counter words
then
    dir_word="directory,"
else
    dir_word="directories,"
fi

if [[ $file_count -eq 1 ]]
then
    file_word="file"
else
    file_word="files"
fi

echo
echo $dir_count $dir_word $file_count $file_word