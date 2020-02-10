# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:27:25 2019

@author: wonju
"""

class Animal :
    def __init__(self, name, age, color) :
        self.name = name
        self.age = age
        self.color = color       
        
    def printInfo(self):
        print(f"name -> {self.name}")
        print(f"age -> {self.age}")
        print(f"color -> {self.color}")
        
class Dog(Animal):
    
    def __init__(self, name, age, color, sound):
        self.name = name
        self.age = age
        self.color = color
        self.sound = sound
    
    def printInfo(self):
        
        super().printInfo()
        print(f'강아지 이름은 {self.name}, 소리를 {self.sound} 냅니다.')
        
dog1 = Dog('안뇽이', 17,'빨간색', '멍멍')
dog1.printInfo()

dog1.age
