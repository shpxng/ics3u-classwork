# Question 1
colour = input("What is your favourite colour? ")

print(f"{colour}? That's my favourite colour too!")

# Question 2
can_in_pack = int(input("How many cans come in a pack? "))

pack = int(input("How many packs are there? "))

total = can * pack

print(f"The total number of cans is {total}")

# Question 3
length = int(input("What is the length of the prism in cm? "))
width = int(input("What is the width of the prism in cm? "))
height = int(input("What is the height of the prism in cm? "))

volume = length * width * height

print(f"The volume of the prism is {volume} cm squared")

# Question 4
print("Do you just join a Google Meet and mute the teacher? Please answer Yes or No")

answer = input("")

if answer == "Yes" :
    print("That's probably not a good idea. You will fail and cry")

else: 
    print("Ok. Good. You deserve cookies")
