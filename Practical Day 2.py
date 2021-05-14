# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:20:43 2021

@author: DAVID ALEN
"""

#Program to find Multiplication table (from 1 to 10) in Python

num = 2


# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
   
   
   
   
# Python program to print Even Numbers in given range
  
start, end = 2, 100
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 == 0:
        print(num, end = " ")
        


# Python program to print odd Numbers in given range
  
start, end = 1, 100
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")
        

#  Program to find Prime Number:   
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)
        
#Python Program to find the multiplication table using for loop
num = int(input("enter the number= "))
i = 1

while i<=10:
    print(num, "X", i, "=", num * i)
    i = i+1
    
# creating a dictionary and print using for loop
d = {'Tekcham ': 1, 'David ': 2, 'Alen': 3}
for k in d:
    print(k)
    
    
    
    
#Condition to check even or odd
num = int(input("Enter a number: "))  
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))  
   