#!/bin/bash

# Alma Beganovic #

usage="Usage: $0 [-o <Outputfile>] <Filename>"

out=""
log=logfile.log

while getopts 'o:' option; do
  case "$option" in
    o) out="$OPTARG"
       ;;
    
    ?) echo "$usage" >&2
       exit 1
       ;;
  esac
done

shift $((OPTIND-1))

if [ $# -eq 0 ]
then 
   echo "Error: missing option" >&2
   echo "Error: missing option" > $log
   echo "$usage" >&2
   exit 0
fi

if [ ! -f $1 ]
then 
    echo "Error: no such file: $1" >&2
    echo "Error: no such file: $1" > $log
    exit 1
fi

PS3="Please choose feature-type: "
O=( $( grep -v "^#" $1 | awk '{print $3}' | sort -u ) )

select opt in ${O[@]}
do
   case $opt in
   "" ) echo "Unknown choice. Try again!"
        echo "Unknown choice. Try again!" > $log
       ;;
   * ) break
       ;;
   esac
done

test -n "$out" && exec > $out

awk 'BEGIN {SUM=0} 
     $3=="'$opt'" {print $0; SUM++} 
     END {print "Summe=",SUM}' $1

{
   date
   echo "Übergabe File: " $1
   echo "User Auswahl: " $opt
   awk 'BEGIN {SUM=0} 
     $3=="'$opt'" {SUM++} 
     END {print "Summe:", SUM}' $1
} > $log
