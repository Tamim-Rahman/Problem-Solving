#problem
#Check if number divisible by 5

#solution
num = int(input("Enter any number: "))

if num % 5 == 0:
    print(f'{num} divisible by 5')
else:
    print(f'{num} is not divisible by 5')