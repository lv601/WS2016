# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:18:20 2016

@author: jose
"""


class Entry:
    def __init__(self, firstname, lastname, age, gender, hobbies, characteristics):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.gender=gender
        self.hobbies=hobbies
        self.characteristics=characteristics
        self.Entry=({"firstname":self.firstname, "lastname":self.lastname, "age":self.age, "gender":self.gender, "hobbies":self.hobbies, "characteristics":self.characteristics})

class Adressbook:
    def __init__(self, Entry):
        self.Entry = Entry
        self.Entries = []
        
        
    def add(self, Entry):
        self.Entries.append(Entry)
        print('Entry was added: {} {}'.format(Entry['firstname'], Entry['lastname']))
        
        
    def get(self, index, key=None):
        if key == None:
            for attribute in self.Entries[index]:
                print(attribute, self.Entries[index][attribute])
            return self.Entries[index]
        else:
            print(self.Entries[index][key])
            return self.Entries[index][key]
        
Adressbook1 = Adressbook({})


Entry1 = Entry("Max", "Musterman", 43, "Male", ["Swimming", "Dance","Read"], {"Skill":10})
Adressbook1.add(Entry1.Entry)
Entry2 = Entry("Jose", "Basilio", 37, "Male", ["Football", "Movies","Read"], {"Skill":130})
Adressbook1.add(Entry2.Entry)
Adressbook1.get(0, "hobbies")
Adressbook1.get(1, "hobbies")
