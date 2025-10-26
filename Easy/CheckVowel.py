#Problem
#Check if char is vowel (a, e, i, o, u)

#Solution

char = input("Enter a character: ").lower()
if char in('a','e','i','o','u'):
    print("It's vowel")
else:
    print("It's not vowel")