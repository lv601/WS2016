#!/bin/bash
if [ $# -eq 0 ]
#if [ $# -lt 2 ]  
#if [ $# -ge 2 ]
then
    echo "parameter fehlt" >&2
else
    echo "Hello World"
fi
