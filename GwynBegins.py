pet = "dog"

**THIS IS FOR concatenation**
string1 = "dogs are"
 string2 = " cute" 
 string3 = string1 + string2 print(string3) 
 age = 12 
 print("you are " + str(age) + " years old.")
 # You need to first convert your integers to a string, then you can concatenate them together. you cannot concatenate an integer into a string. 
 age = input("how old are you? ") 
 print("you are " + age + "years old")
# inputs are automatically accepted as strings # Concatenation can only be done with strings.

 # This works with variables and other strings that haven't been assigned to a variable yet.
  #  Concatenation is accomplished with the plus sign (+) 
  first = "i love"
  second = " grunge" 
  third = " music" 
  combine = (first + second + third)
   print(combine) 
   #  three variables that are assigned to strings.
    a = "python"
     b = "is"
      c = "cool"
       result = a + b + c 
       print(result) 
       # Concatenated the three variables together and store them in a new variable. 
       string1 = "I like to" 
       string2 = "swim." 
       print(string1 + " " + string2)

name = input()
age = input()
birthday = input()

print("Hi " + name + "! You are " + age + " years old and you were born on " + birthday + ".")

name = input()
how_many = input(10)
print(name + how_many)

THIS IS FOR CONVERTING DATA TYPES
name = input("what is your name? ")
age = int(input("what is your age? "))
result = (name * age)
print(result)

THIS IS FOR INPUT OUTPUT MATH
price = int(input("Enter the price of the box: "))
count = int(input("Enter number of granola bars: "))
each_price = price / count
print(each_price)

THIS IS FOR INPUT OUTPUT
dessert = input("Taj")

print("Welcome to the website" + dessert) 

THIS IS FOR NUMBERS
age = 900
rank_outdoors = 8
print(rank_outdoors)
rank_indoors = 10
print(rank_indoors)
time_outdoors = 4.0
print(time_outdoors)
time_indoors = 6.0
print(time_indoors)

THIS IS FOR SYNTAX AND COMMENTS
print("LOTR hobbits")
# its very faithful to the book in certiant aspects
print("M3gan 2.0")
# i loved the story and it was pretty good.
print("The ring")
# I loved how scary it was at the beginning. 

THIS IS FOR Python Geometry
# Bellow is Rectangles And Squares
# rectangle_area = base * height
base = 10
height = 5
rectangle_area = base * height
print(rectangle_area)
# Stop

# Triangles
# The area of a triangle is base times height divided by two.
# triangle_area = (base * height) / 2
base = 10 
height = 5
triangle_area = (10 * 5)/2
print(triangle_area)

# Circles
# The area of a circle uses a value known as pi.
# pi = 3.14 or π = 3.14
circle_area = pi * radius * radius 
# or
circle_area = π * radius * radius

pi = 3.14
radius = 4
circle_area = pi * radius * radius
print(circle_area)

EXAMPLES

side_length = int(input("Enter the side length: "))
square_area = side_length * side_length
print(square_area)

MODULUS
# The percentage sign is used very differently in Python.  This symbol (%) stands for modulus.  The modulus returns the remainder if that number was divided. 
fruits = 10 % 3
print(fruits)
# Determining if a Number is Even or Odd
number = 245
print(number % 2)
# if the remainder is anything other than 0, it must not be an even number.

STINGS
# A string is a piece of information with quotation marks around it. 
# Strings can also have numbers in them.
candy = "I have 10 chocolate candies and 13 strawberry candies."
# Strings can also be many words long.
# Strings can also just have numbers in them.
age = "15"
# try to do math with a string, we run into problems.
# Strings can also be called string literals.
# Strings can also hold a large amount of text that goes across multiple lines of code. These are called multiline strings. To create a multiline string, you must use three sets of quotes, double or single, before and after the desired text.
string1 = """i am a long code vro.
test me out mayn
im so cool and stuff 
i can also be used with single quotes"""
# sometimes a string is so long that it wraps around and forms a new line. 
multiline = ''' lol im super long string
i can keep going
and ill be the same variable anyways vro'''


