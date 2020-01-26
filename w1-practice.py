import math
import random

def new_section(title):
    length = len(title)
    max_len = 50
    hyphens_all = max(max_len - length - 2, 0) # string multiplication with negative returns empty string
    hyphens_half = hyphens_all //2
    section = f"\n{'-' * hyphens_half } {title} {'-' * (hyphens_all - hyphens_half)}\n"
    print(section)

# miles to feet
def miles_to_feet(miles):
    feet = miles * 5280
    return round(feet)

new_section("Miles to feet")
miles = 1.4
print(f"{miles} miles = {miles_to_feet(miles)} ft.")

# Hours to seconds
new_section("Hours to seconds")

def hours_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s
hours = 4
minutes = 10
seconds = 3
print(f"{hours} hours, {minutes} minutes, {seconds} seconds are {hours_to_seconds(hours, minutes, seconds)} seconds")

# Rectangle perimeter
new_section("Rectangle perimeter")

def rectangle_perimeter(w, h):
    return round((w + h) * 2, 2)

width = 22.233
height = 30
print(f"A rectangle with w = {width} and h = {height} will have the {rectangle_perimeter(width, height)} perimeter")

# Rectangle area
new_section("Rectangle area")

def rectangle_area(w, h):
    return round(w * h, 2)

width = 25
height = 5
print(f"A rectangle with w = {width} and h = {height} will have the {rectangle_area(width, height)} area")

# Circle circumference
new_section("Circle circumference")

def circle_circumference(radius):
    return round(2 * radius * math.pi, 2)

radius = 30

print(f"The circumferece of a circle with the radius {radius} is {circle_circumference(radius)}")

# Circle area
new_section("Circle area")

def circle_area (radius):
    return round(radius ** 2  * math.pi, 2)

print(f"The area of a circle with the radius {radius} is {circle_area(radius)}")

# Future value
new_section("Future value")

def future_value(value, rate, years):
    return round(value * (1 + rate) ** years, 2)

present_value = 1200
annual_rate = 0.01
years = 30

print(f"With {present_value}, with the annual rate of {annual_rate}, I'll have {future_value(present_value, annual_rate, years)} in {years} years")

# Name tag
new_section("Name tag")

def name_tag(first, last):
    print(f"My name is {first} {last}")

first_name = "Michael"
last_name = "Mikhailovi\N{latin small letter c with acute}"

name_tag(first_name, last_name)

# Name and age
new_section("Name and age")

def name_and_age(n, a):
    print(f"{n} is {a} years old.")

name = "Michael Mikhailovi\N{latin small letter c with acute}"
age = 45

name_and_age(name, age)


# Point distance
new_section("Point distance")

def point_distance(x0, y0, x1, y1):
    return round(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5, 2)

x0 = 0
y0 = 3
x1 = 6
y1 = 4

print(f"The distance btw. P{x0, y0} and P{x1, y1} is {point_distance(x0, y0, x1, y1)}")


# Triangle area
new_section("Triangle area")

def triangle_area(x1, y1, x2, y2, x3, y3):
    a = point_distance(x1, y1, x2, y2)
    b = point_distance(x1, y1, x3, y3)
    c = point_distance(x2, y2, x3, y3)
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)


x0 = 0
y0 = 3
x1 = 6
y1 = 4
x2 = 3
y2 = 2

print(f"For trianngle with coordinates {x0, y0}, {x1, y1}, and {x2, y2}, triangle area is {triangle_area(x0, y0, x1, y1, x2, y2)}")


# Print digits
new_section("Print digits")

def print_digits(number):
    tens = number // 10
    ones = number % 10
    print(f"The tens digit is {tens} and the ones digit is {ones}")

number = 95

print_digits(number)

# Powerball

def ball():
    return random.randrange(1, 60)

def powerball():
    message = f"Today's numbers are {ball()}, {ball()}, {ball()}, {ball()}, and {ball()}. The Powerball number is {ball()}."
    print(message)

powerball()
