print(5+5)
print(10+10)
print(73+49)
print(423+57)
print(87+23)

print(39-53)
print(22-11)
print(85-98)
print(44-32)
print(21-3)

print(4*2)
print(9*4)
print(1*3)
print(80*65)
print(41*67)

print(4/2)
print(5/1.5)
print(8/3)
print(500/2)
print(420/9)

print(8%5)
print(7%2)
print(9%2)
print(500%43)
print(87%5)

print(5**2)
print(8**8)
print(6**21)
print(9**2)
print(7*17)

print(5//2)
print(8//3)
print(327//3)
print(789//21)
print(523//21)

#You might have noticed certain symbols being repeated.
#Those are, of course, / and *.
#/ * and // ** and different from eachother, though.
#They're similiar in purpose, but not how they actually calculate.
#For example, * and ** both multiply numbers, as does / and // with dividing numbers.
#The difference is, * multiplies the numbers in the print() command. So if we put in print(8*9), it would multiply 8 and 9. However, add another *,
#and now it multiplies 8 to the power of 9.
#So while they both multiply, * multiplies the given numbers, while ** multiplies to the power of the given number.
#For / and //, they're more alike, but still very distinct and it is extremely important to not confuse the two.
#/ divides the numbers, and gives the whole result, and ALWAYS includes the decimal after, even if it is zero, and turns the number into a floater.
#// however, does not. It always removes the decimal after (even if the decimal is greater than .0, by rounding up 0.1 to 0.5 back to 0 for this example, but if it's greater than 0.5, it rounds it up to 1.), and keeps the number as an integer. 
#To put it more in perspective,
# 5/2 = 2.5 (int)
# 5//2 = 2 (int)
# 6/2 = 3.0 (floater)
# 6 / 2 = 0 (floater)

#temperatures now

C = 50
F = (C*9/5)+32
K = (C+273.15)

print("What's the temperature in Celsius like?")
print(C)
print("What's the temperature in Fahrenheit if the current temperature in Celsius is 50?, Let's find out.")
print(F)
print("What's the temperature in Kelvin if the current temperature in Celsius is 50?, Let's find out.")
print(K)

#okay, temperatures done, lets finish this off with the terminal thing now

first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
city_name = input("Enter name of city: ")

print(f"Hello, {first_name} {middle_name} {last_name}. You are {age} years old, and live in the city of {city_name}. It's a pleasure to meet you.")


