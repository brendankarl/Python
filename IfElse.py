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

#If statement with and, if product1 sales is greater than that of product1 and product2 then print the statement
product1sales = 100
product2sales = 200
product3sales = 300

if product3sales > product2sales and product1sales:
    print("product3sales is is greater than product1sales and product2sales")

#Or statement, if product2sales is greater than product1sales or product3sales print true
product1sales = 100
product2sales = 200
product3sales = 300

if product2sales > product1sales or product3sales:
    print("true")