# 1
def add_3_numbers(a: int, b: int, c: int) -> int:
    return a + b + c

#2
def return_name_age(name: str, age: int) -> str:
    return f"Name: {name}. Age: {age}"

#3
def calc_average(a: int, b: int) -> int:
    return (a + b) / 2

#4
def return_largest(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a

    elif b > a and b > c:
        return b

    else:
        return c

#5
def first_2_char(string: str) -> str:
    return string[:2]
