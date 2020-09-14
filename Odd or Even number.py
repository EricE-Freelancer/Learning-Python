#Odd or Even number
#A number is even if division by 2 gives a remainder of 0.
#A number is odd if division by 2 gives a remainder of 1.

whole_number = int(input("Enter a whole number: "))
result = whole_number % 2  #a number mod to 2, the result will either 1 or 0

if result ==0: #the remainder output 0 will be even
    print(whole_number, "is an even number")
elif result ==1: #the remainder output 1 will be odd
    print(whole_number, "is an odd number")
else:
    print(whole_number, "is a Invalid input")




