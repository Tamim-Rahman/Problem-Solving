#Problem
#Convert temperature string "25C" to number 25

#Solution
temp = "25C"
number = int(temp[:-1])
print(number)
print(type(number))