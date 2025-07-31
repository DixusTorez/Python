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

STRING METHODS
# Methods are keywords which a program can use to modify data within a variable. To use a method on a variable, you must type the name of the variable then type a period and the name of the method you wish to use. After the name of the method you must type opening and closing parentheses.
string1.methodname()

# The lower and upper methods are used to make all characters in a string change to be either lowercase or uppercase.
strin1 =  "I love Coding!"
print(strin1.lower())
print(strin1.upper())

# The replace method changes a specified character or characters (letters, numbers, or symbols) in the string to something else. 
string1 = "Coding is cool!"
print(string1.replace("cool", "fun"))

# strip method can be used to remove any excess white space at the beginning or end of a string. 
string1 = " I love Coding! "
print(string1.strip()) 

# index number is a number that says where a character is in a string. While indexing, we start counting at zero.
# the first character is always zero 
string1 = "coding is awsome"
print(string1[5])

# spaces also count as a character
# you can go backwards by using negatives Notice that when indexing from the end you start counting at one, not zero.
string1 = "coding is awsome"
print(string1[-5])

# Slicing is when we use the indexes to print specific "slices" of a string. To do this, we use colons in the brackets. The first number is the index to start at, and the second number is where to end. 
string1= "i love coding!"
print(string1[4:9])
# If a section is left blank, it will go either to the beginning or the end of the string.
string1= "i love coding!"
print(string1[:9])

# To reverse a string, you start slicing at the end of the string and work backwards.  Moving back through the string with a negative number in the third number slot will pull out each letter in turn from back to front.
string1 = "yodel"
reverse = string1[len(string1)::-1]
print(reverse)

# how to split a string
string1 = "yodel ey yehooo"
print(string1.split())

# how to see the length of a string
string1 = "yodel ey yehooo"
print(len(string1))

# how to Find a Character in a String. will return a number and that will be where it is
string1 = "Mississippi" 
print(string1.find("s"))
# tell it to start from the back with .rfind

CHECKING STRINGS
# Checking a string is really simple! It's done by using the keyword "in" as shown below.
string1 = "i love coding!"
check = "lone" in string1
print(check)
# output should be true
# checking is a boolean!
# you can use the keywords "not in" to check to see whether or not the string is present in the variable. 
string1 = "i love coding!"
check = "love" not in string1
print(check)
#output should be false

Concatenating NUMBERS
# Concatenation doesn't work the same way with numbers. This is because the plus sign is also used to do basic math functions. 
# he method which helps you combine different variable types with strings is called the "format()" method.
# combining strings with integers? This is called the format method. 

# string1.format( )
# This function is expecting a variable to be placed within the parenthesis which can then be converted into the variable as shown below

# string1.format(age)
# You can also use multiple integers inside the format method.

string1 = "The number of miles we've hiked totals up to {}"
miles = 21
print(string1.format(miles))

string1 =  "the number of miles we've hiked totals up to {} which is {} feet"
miles = 21
feet = 110880
print(string1.format(miles, feet))
# examples 
# Input for number of apples from one tree
apples_per_tree = float(input("Enter the number of apples from one tree: "))

# Bob has 3 wheelbarrows and 8 trees
wheelbarrows = 3
trees = 8

# Calculate apples per wheelbarrow for one tree and for the whole orchard
per_wheelbarrow_one_tree = float(apples_per_tree / wheelbarrows)
per_wheelbarrow_orchard = float((apples_per_tree * trees) / wheelbarrows)

# Output using format method
output = "If Bob harvested one tree, he would have {} apples per wheelbarrow. If he harvested the whole orchard, he would have {} apples per wheelbarrow.".format(per_wheelbarrow_one_tree, per_wheelbarrow_orchard)

print(output)
# The format can actually handle an unlimited number of variables within the parenthesis. This is done by separating each variable with a comma. The example below shows how this is done.

LIST
# In Python, there are 3 main ways to group data together:

# List: a data group that is ordered (numbered) and changeable (you can change the list items).  Allows duplicates.

# Tuple: a data group that is unordered and unchangeable.  Allows duplicates.

# Dictionary: a data group that is unordered, changeable and indexed.  No duplicates.

# A listA group of data that uses [ ] brackets and can be changed. in Python is a data group that is ordered and changeable. 

# Ordered means that the order of the data in the group matters.  Changeable means that you can switch out the data points right in the middle of your list. For example, the order of a step-by-step list of directions matters
