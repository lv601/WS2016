#!/usr/bin/env python3    # shebang needed in executeable files. chmod 755
stringA="Haus"
stringB="katze"
print(stringA+stringB)
#print(stringA-stringB)  #TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(stringA*stringB)   #TypeError: can't multiply sequence by non-int of type 'str'
#print(stringA/stringB)    #TypeError: unsupported operand type(s) for /: 'str' and 'str'

#print(stringA+4)         #TypeError: Can't convert 'int' object to str implicitly
#print(stringA-4)     #TypeError: unsupported operand type(s) for -: 'str' and 'int'
print(stringA*4)       #HausHausHausHaus
#print(stringA/4)       #TypeError: unsupported operand type(s) for -: 'str' and 'int'


print('int(15)/3.5'+' = '+str(int(15)/3.5))
print(type(int(15)/3.5))
print('\n')
print('int(15)//3.5'+' = '+str(int(15)//3.5))
print(type(int(15)//3.5))
print('\n')
print('int(15)/4'+' = '+str(int(15)/4))
print(type(int(15)/4))
print('\n')
print('int(15)//4'+' = '+str(int(15)//4))
print(type(int(15)//4))