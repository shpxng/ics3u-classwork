# 1.
# Ask user for favourite color
colour = input("What is your favourite colour? ")

# Output a message
print(colour, "That's my favourite colour too!")

# 2.
# Ask user for number of cans
can = int(input("How many cans come in a pack? "))

# Ask user for number of packs
pack = int(input("How many packs are there? "))

# Calculate total number
total = can * pack

# Display total number of cans
print(f"The total number of cans is {total}")


# 3.
# Ask user for dimensions of a rectangular prism
length = int(input("What is the length of the prism in cm? "))
width = int(input("What is the width of the prism in cm? "))
height = int(input("What is the height of the prism in cm? "))

# Display the volume of the prism
print("The volume of the prism is", length * width * height, "cm squared")
