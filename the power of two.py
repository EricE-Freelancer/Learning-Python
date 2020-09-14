print("Hi! what is your name? ")
name = input()

anything = float(input("Hi " + name + ", Enter a number: "))
something = anything ** 2.0

print("nice to meet you " + name +"!")
print(anything, "to the power of 2 is", something)

#the float() function takes one argument (e.g., a string: float(string))and tries to convert it into a float
#because we are inputing a number = float
#input = string or alphabet only
