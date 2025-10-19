#Problem
#Check if string is palindrome (e.g., "madam")

#Solution

text = input("Enter any word to check palindrome: ")
print("Palindrome:", text == text[::-1])