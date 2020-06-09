print("test")

#Now lets show how to use an escape sequence, notice the syntax below will add a single double quote into the string, we are escaping the string and adding a double quote
#If we did not add the backslash, python would treat it as the end of the string rather than a literal double quote to print on the screen. 
print("test \" value")

number = 999
number_as_string = str(number)
print(number_as_string)

#Here are some examples of doing string contatenation, some with new Python v3 Syntax

#Example 1:
week = 33
welcomePromt = "Greetings, it is week " + str(week) + " of the year"
print(welcomePromt)

#Example 2: Same example different syntax
week = 33
print("Greetings, it is week {week} of the year".format(week=week))

#Example 3: Python3 syntax
week = 33
print(f"Greetings, it is week {week} of the year")


