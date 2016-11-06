# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:55:20 2016

@author: jose
"""

import time, io


def repeat_string1(string="Test", repeat=10000):
    str_io=io.StringIO()
    
    for i in range(repeat):
        str_io.write(string)
    
    return str_io.getvalue()

def repeat_string2(string="Test", repeat=10000):
    str_imm=""
    
    for i in range(repeat):
        str_imm +=string
        
    return str_imm
    
def time_counter(func, *args, **kargs):
    start=time.time()
    result=func(*args, **kargs)
    end=time.time()
    print('Function {} takes {:.5} seconds'.format(func.__name__, end-start))
    return result
    
t1 = time_counter(repeat_string1, repeat=10000)
t2 = time_counter(repeat_string2, repeat=10000)


    