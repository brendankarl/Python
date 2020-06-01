#Basic Example Try, Except (catch), Else and Finally
name = "Harrison"

try:
    print(name)
except:
    print("-Error Found")
else:
    print("-No Errors Found")
finally:
    print("-Last thing to run")

#Basic example with failure - "name2" doesn't exist
try:
    print(name2)
except:
    print("-Error Found")
else:
    print("-No Errors Found")
finally:
    print("-Last thing to run")

#Raise an exception manually
num = 5

if num < 6:
    raise Exception("Number must be greater than 5")

#Integrate into Try, Except - if the entered number is less than 6 generate an exception
number = input("Enter Number...")

try:
   if int(number) < 6:
       raise Exception("Number must be greater than 5") 
except:
    print("Error Found")
finally:
    print("The number you entered was " + number)