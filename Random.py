import random

#Generate random number between 0 and 1
random.random()

#Generate random number between 1 and 10
random.randint(1,10)

#Generate random number between 1 and 10 (with a step of 2) therefore 1,3,5,7,9
random.randrange(1,10,2)


#Select random item from list
colours = ["red","blue","green","yellow"]
colours[random.randrange(0,len(colours))] #use the length of the list to set the range