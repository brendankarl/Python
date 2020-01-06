#For loop with list
names = ["brendan","lewis","harrison"]
for name in names:
    print(name)

#For loop with list and break - will only print items in the list up until Lewis and will then break out of the loop
names = ["brendan","lewis","harrison"]
for name in names:
    print(name)
    if name == 'lewis':
        break

#For loop with list and continue - include an IF statement for Lewis and then do something, then continur
names = ["brendan","lewis","harrison"]
for name in names:
    print(name)
    if name == 'lewis':
        print('*CONTINUE*')
        continue

#For loop using the range function to loop through everything apart from the last item in the list and print
names = ["brendan","lewis","harrison"]
for name in range(len(names)-1):
    print(names[name])

#Nested loop loop through names and for each print along with the items in colours
names = ["brendan","lewis","harrison"]
colours = ["red","blue","green"]
for name in names:
    for colour in colours:
        print(name, colour)

#For loop iterating over files in a drive
import os
for files in os.walk("D:\\"):
    print(files)

#While loop, print the number until it is 6
number = 1
while number < 6:
    print(number)
    number += 1

#While loop with break statement, break when the number is equal to 5
number = 1
while number < 10:
    print(number)
    if number == 5:
        break
    number += 1

#While loop with continue statement, do something when the number is equal to 7
number = 1
while number < 10:
    print(number)
    number += 1
    if number == 7:
        print('*CONTINUE*')
        continue  