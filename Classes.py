class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def printperson(self):
        print("Hello" + self.name)

#Create object
p1 = Person("Brendan",38,"male")

#Call printperson() function to print name
printperson(p1)

#Change age to 39
p1.age = 39
p1.age

#Delete gender
del p1.gender