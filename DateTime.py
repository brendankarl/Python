import datetime

DateString = "2021-05-06 00:00:00" #Date String
DateObject = datetime.datetime.strptime(DateString, "%Y-%m-%d %X") #Convert to DateTime Object
DateObject.strftime("%B") #Output Month Name
DateObject.strftime("%A") #Output Day Name
DateObject.strftime("%j") #Output Day Number within Year
#Full reference of directives - https://www.w3schools.com/python/python_datetime.asp