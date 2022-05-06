#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Lenovo
#
# Created:     06/05/2022
# Copyright:   (c) Lenovo 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# while loop
i=5
while i>=0:
    print(i* "  bhuppi")
    i=i-1
#for loop
for i in range(5):
    print(i+ 1)
#list - collection of items[]
marks= [95,96,90]
marks.insert(1,99)
marks.append(99)
#print(marks[1:3])
for score in marks:
    print(score)
print(99 in marks)
print(len(marks))

while i<len(marks):
    print(marks[i])
    i=i+1
marks.clear()
print(marks)
#break and continue
students= ["ram","shytam","kishan","aman"]
for student in students:
    if student == "kishan":
        continue;
print(student)

#tuple()
marks = (90,98,96,98)
print(marks.count(98))
#set{}- it dos'nt contain index that's why called unordered
marks= {"aman","amna","amna"}
print(marks)
#dictionary- similar to set
marks= {"english":99,"chemistry":90}
print(marks["chemistry"])
marks["physcis"]= 97
print(marks)
