#Basic if statement, will only print out the name if it is Brendan otherwise, it will print "not Brendan"
names = ["brendan","lewis","harrison"]
for name in names:
    if name == "brendan":
        print(name)
    else:
        print("not Brendan!")   

#If statement with elif (else if) and else, will handle brendan, lewis and harrison differently, any other names in the names list will print "Blah!"
names = ["brendan","lewis","harrison","james"]
for name in names:
    if name == "brendan":
        print(name)
    elif name == "lewis":
        print("l")
    elif name == "harrison":
        print('H')
    else:
        print("Blah!")