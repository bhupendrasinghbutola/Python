#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Lenovo
#
# Created:     06/05/2022
# Copyright:   (c) Lenovo 2022
# Licence:     <your licence>
#---------
#if else
age= 12
if age >= 18:
    print("you are adult")
    print("you can vote")
elif age<18 and age>3:
    print("you are in school")
else:
    print("thhanks")

#mini calculator
firstNum=input("enteer the first num")
secNum= input("enter the second num")
operator=input("enter operator(+,-,*,/)")
if operator=='+':
    sum= int(firstNum)+int(secNum)
    print("you added" , firstNum , operator , secNum , '=', str(sum))
elif operator=='-':
    sum= int(firstNum)-int(secNum)
    print("you subtracted" , firstNum , operator , secNum , '=', str(sum))
elif operator=='*':
    sum= int(firstNum)*int(secNum)
    print("you multiplied" , firstNum , operator , secNum , '=', str(sum))
elif operator=='//':
    sum= int(firstNum)//int(secNum)
    print("you divided" , firstNum , operator , secNum , '=', str(sum))
else:
    print("you have entered string")