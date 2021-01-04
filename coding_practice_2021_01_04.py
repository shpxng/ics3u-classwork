# Exercise 81
import math

def two_shorter_sides(a: int, b: int):
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    return hypotenuse

def main():
    a = int(input("Enter length of first side: "))
    b = int(input("Enter length of second side: "))
    get_sides = two_shorter_sides(a, b)
    print(get_sides)

# Exercise 82
def taxi_fare(dis: int):
    fare = 4 + ((dis // 140) + (dis % 140 > 0)) * 0.25
    return fare

def main():
    dis = int(input("Enter kilometers traveled: "))
    dis_in_meters = dis * 1000
    total_cost = taxi_fare(dis_in_meters)
    print(total_cost)

