# Exercise 36

letter = input("Please enter a letter in the alphabet: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter entered is a vowel")

elif letter == "y":
    print("The letter entered is sometimes a vowel and sometimes a consonant")

else:
    print("The letter entered is a consonant")
    
# Exercise 37

side_number = int(input("Please enter the number of sides of a shape between 3 and 10: "))

if side_number == 3:
    shape = "Triangle"
     
elif side_number == 4:
    shape = "Square"
        
elif side_number == 5:
    shape = "Pentagon"
            
elif side_number == 6:
    shape = "Hexagon"

elif side_number == 7:
    shape = "Heptagon"

elif side_number == 8:
    shape = "Octogon"

elif side_number == 9:
    shape = "Nonogon"

elif side_number == 10:
    shape = "Decagon"

else:
    print("Error. Please enter a number between 3 and 10")

print(f"Your shape is a {shape}")
    
# Exercise 38

month = input("Please enter a month: ")

if month == "February":
    print("Number of days: 28 or 29 days")

elif month == "April" or month == "June" or month == "September" or month == "November":
    print("Number of days: 30 days")

elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("Number of days: 31 days")

else:
    print("Error. Please enter a month")

# Exercise 40

first_side = int(input("Please enter the length of the first side: "))
second_side = int(input("Please enter the length of the second side: "))
third_side = int(input("Please enter the length of the third side: "))

if first_side == second_side == third_side:
    print("The triangle is an equilateral triangle")

elif first_side == second_side or first_side == third_side or second_side == third_side:
    print("The triangle is an isosceles triangle")

else:
    print("The triangle is a scalene triangle")
    
# Exercise 43

dollar = int(input("Please enter the denomination of a banknote($): "))

if dollar == 1:
    individual = "George Washington"

elif dollar == 2:
    individual = "Thomas Jefferson"

elif dollar == 5:
    individual = "Abraham Lincoln"
    
elif dollar == 10:
    individual = "Alexander Hamilton"
    
elif dollar == 20:
    individual = "Andrew Jackson"

elif dollar == 50:
    individual = "Ulysses S. Grant"

elif dollar == 100:
    individual = "Benjamin Franklin"
else:
    print("Error. Banknote does not exist")
    
print(f"The individual on the banknote is {individual}")

# Exercise 47

month = input("Please enter your month of birth: ")
date = int(input("Please enter your date of birth: "))

if month == "January":
    if date <= 19:
        sign = "Capricorn"
    elif date >= 20:
        sign = "Aquarius"

if month == "February":
    if date <= 18:
        sign = "Aquarius"
    elif date >= 19:
        sign = "Pisces"

if month == "March":
    if date <= 20:
        sign = "Pisces"
    elif date >= 21:
        sign = "Aries"

if month == "April":
    if date <= 19:
        sign = "Aries"
    elif date >= 20:
        sign = "Taurus"

if month == "May":
    if date <= 20:
        sign = "Taurus"
    elif date >= 21:
        sign = "Gemini"

if month == "June":
    if date <= 20:
        sign = "Gemini"
    elif date >= 21:
        sign = "Cancer"

if month == "July":
    if date <= 22:
        sign = "Cancer"
    elif date >= 23:
        sign = "Leo"

if month == "August":
    if date <= 22:
        sign = "Leo"
    elif date >=23:
        sign = "Virgo"

if month == "September":
    if date <= 22:
        sign = "Virgo"
    elif date >= 23:
        sign = "Libra"

if month == "October":
    if date <= 22:
        sign = "Libra"
    if date >= 23:
        sign = "Scorpio"

if month == "November":
    if date <= 21:
        sign = "Scorpio"
    if date >= 22:
        sign = "Sagittarius"

if month == "December":
    if date <= 21:
        sign = "Sagittarius"
    if date >= 22:
        sign = "Capricorn"

print("Your Zodiac Sign is" , sign)

# Exercise 49

magnitude = float(input("Please enter an earthquake magnitude: "))

if magnitude < 2:
    descriptor = "micro"

elif magnitude <3:
    descriptor = "very minor"

elif magnitude <4:
    descriptor = "minor"

elif magnitude <5:
    descriptor = "light"

elif magnitude <6:
    descriptor = "moderate"

elif magnitude <7:
    descriptor = "strong"

elif magnitude <8:
    descriptor = "major"

elif magnitude <10:
    descriptor = "great"

else:
    descriptor = "meteoric"

print("A" , magnitude, "is a" , descriptor, "earthquake")
