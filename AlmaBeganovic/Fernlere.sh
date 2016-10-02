#!/bin/bash
if [ $# -eq 0 ]
#if [ $# -lt 2 ]  
#if [ $# -ge 2 ]
then
    echo "parameter fehlt" >&2
else
    echo "Hello World"
fi


usage="$0 [-o] <Filename>"
if [ $# -eq 0 ]
then 
   echo "missing option" >&2
   echo "$usage" >&2
   exit 0
fi

while getopts ':o' option; do
  case "$option" in
    o) echo "Hello World o" >>file.txt
       exit
       ;;
    :) printf "missing argument for -%s\n" "$OPTARG" >&2
       #printf "missing argument for -%s\n" "$OPTARG" >&2 >>file.txt 2>&1
       echo "$usage" >&2
       exit 1
       ;;
   \?) printf "illegal option: -%s\n" "$OPTARG" >&2
      # printf "illegal option: -%s\n" "$OPTARG" >&2 >>file.txt 2>&1
       echo "$usage" >&2
       exit 1
       ;;
  esac
done
