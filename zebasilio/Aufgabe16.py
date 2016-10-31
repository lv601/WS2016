# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:50:15 2016

@author: jose and ClemensBioinf
"""

class Entry:
    def __init__(self, firstname, lastname, hobbies, age, characteristics, gender):
        self.firstname=firstname
        self.lastname=lastname
        self.hobbies=hobbies
        self.age=age
        self.characteristics=characteristics
        self.gender=gender
        
        
        self.Entry=({"firstname":self.firstname, "lastname":self.lastname, "age":self.age, "gender":self.gender, "hobbies":self.hobbies, "characteristics":self.characteristics})




    def __str__(self):
        def multi_format(attribute):
            multi_format = '\n'
            for element in attribute:
                multi_format += '\t- {}\n'.format(element)
            return multi_format.rstrip('\n')
            
            
        return 'Entry\n============================\nfirstname: {0.firstname}\nlastname: {0.lastname}\
        \nhobbies: {1}\nage: {0.age}\ncharacteristics: {2}\ngender: {0.gender}\n=============================='\
        .format(self, multi_format(self.hobbies), multi_format(self.characteristics))
        
    def __bytes__(self):
        return self.__str().encode()
        
    def __repr__(self):
        return "Entry('{0.firstname}', '{0.lastname}', '{0.hobbies}', '{0.age}', '{0.characteristics}', '{0.gender}')"\
        .format(self)
        
ins = Entry('Max', 'Mustermann',['walk', 'run', 'paint'], 20, ['funny', 'unselfish'], 'male')

print(ins)
#print(repr(ins))


            