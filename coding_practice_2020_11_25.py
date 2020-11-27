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

# Exercise 39

sound = int(input("Please enter a sound level in decibels: "))

if sound == 40:
    print("Noise level of a Quiet Room")

elif sound == 70:
    print("Noise level of an Alarm Clock")

elif sound == 106:
    print("Noise level of a Gas lawnmower")

elif sound == 130:
    print("Noise level of a Jackhammer")

elif sound < 40:
    print("Noise level is less than a Quiet Room")

elif sound > 40:
    print("Noise level is between a Quiet Room and an Alarm Clock")

elif sound > 70:
    print("Noise level is between an Alarm Clock and a Gas Lawnmower")

elif sound > 106:
    print("Noise level is between a Gas Lawnmower and a Jackhammer")

elif sound > 130:
    print("Noise level is greater than a Jackhammer")
    
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

# Exercise 48

year = int(input("Please enter a year: "))

if year%12 == 4:
    animal = "rat"

elif year%12 == 5:
    animal = "ox"

elif year%12 == 6:
    animal = "tiger"

elif year%12 == 7:
    animal = "hare"

elif year%12 == 8:
    animal = "dragon"

elif year%12 == 9:
    animal = "snake"

elif year%12 == 10:
    animal = "horse"

elif year%12 == 11:
    animal = "sheep"

elif year%12 == 0:
    animal = "monkey"

elif year%12 == 1:
    animal = "rooster"

elif year%12 == 2:
    animal = "dog"

elif year%12 == 3:
    animal = "pig"

else: 
    print("Invalid year")

print(animal)

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

# Exercise 51

letter = input("Please enter a letter grade: ")
letter = letter.upper()

if letter == "F":
    gpa = "0"

elif letter == "D":
    gpa = "1.0"

elif letter == "D+":
    gpa = "1.3"

elif letter == "C-":
    gpa = "1.7"

elif letter == "C":
    gpa = "2.0"

elif letter == "C+":
    gpa = "2.3"

elif letter == "B-":
    gpa = "2.7"

elif letter == "B":
    gpa = "3.0"

elif letter == "B+":
    gpa = "3.3"

elif letter == "A-":
    gpa = "3.7"

elif letter == "A" or letter == "A+":
    gpa = "4.0"

else:
    gpa = "Invalid"

print(f"Your Grade Point Average is {gpa}")

# hello_name

name = input("Enter name: ")

print(f"Hello {name}!")

# make_abba

str1 = input("Enter a string: ")
str2 = input("Enter a second string: ")

print(str1 + str2 + str2 + str1)

# make_out_word

out = input("Enter an out string of length 4: ")
word = input("Enter a word: ")

print(out[0] + out[1] + word + out[2] + out[3])

# extra_end

str = input("Enter a word: ")

last_char = str[-1]
second_last_char = str[-2]

print(second_last_char + last_char + second_last_char + last_char + second_last_char + last_char)

# without_end

str = input("Enter a string: ")

print(str[1:-1])

# non_start

str1 = input("Enter a string: ")
str2 = input("Enter a second string: ")

str1_omitted = str1[1:-1] + str1[-1]
str2_omitted = str2[1:-1] + str2[-1]

print(str1_omitted + str2_omitted)

# left_2

str = input('Enter a string: ')

first_two_char = str[0] + str [1]
end = str[2:-1] + str [-1]

print(end + first_two_char)

# right_2

str = input("Enter a string: ")

last_two_char = str[-2] + str[-1]
front = str[0:-2]

print(last_two_char + front)

# ends_ly

str = input("Enter a string: ")

if str[-2] == "l" and str[-1] == "y":
    print("True")

else:
    print("False")
    
# con_cat

str1 = input("Enter a string: ")
str2 = input("Enter a second string: ")

if str1[-1] == str2[0]:
    print(str1[0:-1] + str2)

else:
    print(str1 + str2)
