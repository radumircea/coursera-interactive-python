# Week 2 Practice Set

def new_section(title):
    length = len(title)
    max_len = 50
    hyphens_all = max(max_len - length - 2, 0) # string multiplication with negative returns empty string
    hyphens_half = hyphens_all //2
    section = f"\n{'-' * hyphens_half } {title} {'-' * (hyphens_all - hyphens_half)}\n"
    print(section)

new_section("Is Even")

def is_even(number):
    remainder = number % 2
    if remainder == 0:
        return True
    else:
        return False

number = 123
number_2 = 1000
print(f"Is {number} even?: {is_even(number)}")
print(f"Is {number_2} even?: {is_even(number_2)}")

new_section("Is Cool")

def is_cool(name):
    """ Check if teacher is cool """
    if name == "Joe" or name == "John" or name == "Stephen":
        return True
    else:
        return False

teachers = ["Joe", "John", "Stephen", "Scott"]

print(f"Is this {teachers[3]} cool? {is_cool(teachers[3])}")


new_section("Is lunchtime")

def is_lunchtime(hour, is_am):
    """ Check if 11am or 12pm"""
    return (hour == 11 and is_am) or (hour == 12 and not is_am)

hour = 11
is_am = True

print(f"Is it time for lunch? {is_lunchtime(hour, is_am)}")

new_section("Is leap year")

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
year = 1904
print(f"Is {year} leap year? {is_leap_year(year)}")


new_section("Interval intersect")

def interval_intersect(a, b, c, d):
    """ Check if intervals [a, b], [c, d] intersect. a<=b, c<=d """
    return a <= d or c <= b

a = 4
b = 5
c = 2
d = 5
print(f"Do these intersect : [{f'{a} {b}'}] and [{f'{c} {d}'}]? {interval_intersect(a, b, c, d)}")

new_section("Name and age")

def name_and_age(name, age):
    if age < 0:
        return "Error! Invalid age."
    else:
        return f"{name} is {age} years old."

print(f"Introduction: {name_and_age('Michael', 99)}")


new_section("Print digits")

def print_digits(number):
    """ Print digits for 0 <= int < 100 """
    if number < 0 or number >= 100:
        print("Error: Input is not a two digit or positive number.")
    else:
        tens = number // 10
        ones = number % 10
        return f"The tens digit is {tens} and the ones digit is {ones}"

print(print_digits(-1))
print(print_digits(100))
print(print_digits(9))

new_section("Name lookup")

def name_lookup(first_name):
    if first_name == "Joe":
        return "Warren"
    elif first_name == 'Scott':
        return 'Rixner'
    elif first_name == 'John':
        return 'Greiner'
    elif first_name == 'Stephen':
        return 'Wong'
    else:
        return 'Error! Not an instructor.'

print(f"Find last name for Joe:", name_lookup('Joe'))
print(f"Find last name for Scott:", name_lookup('Scott'))
print(f"Find last name for John:", name_lookup('John'))
print(f"Find last name for Stephen:", name_lookup('Stephen'))
print(f"Find last name for William:", name_lookup('William'))

new_section("Pig Latin")

def pig_latin(word):
    first = word[0].lower()
    rest = word[1:]
    if first == 'a' or first == 'e' or first == 'i' \
                    or first == 'o' or first == 'u':
        return word + 'way'
    else:
        return rest + first + 'ay'
    
print(pig_latin("owl"))
print(pig_latin("pig"))
print(pig_latin("python"))

new_section("Smaller Root")

def smaller_root(a, b, c):
    """ Return smaller solution to the quadratic formula: ax**2 + bx + c = 0 """
    """ x = [-b +- math.sqrt(b**2 - 4ac)] / 2a """
    denominator = 2 * a
    discriminant = (b**2 - 4 * a * c)
    if discriminant < 0:
        print("Error: No real solutions")
    else:
        smaller = min( 
            (-b - discriminant**0.5) / denominator,
            (-b + discriminant**0.5) / denominator
        )
        return smaller

print(smaller_root(1, 2, 3))
print(smaller_root(2, 0, -10))
print(smaller_root(6, -3, 5))