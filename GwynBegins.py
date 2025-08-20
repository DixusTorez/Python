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

IF STATEMENT FOR A LOOP

# You can put any code you want inside a for loop. For loops get really fun when we add in an if statement. The loop moves through a list and checks to see if each item in the list fits a conditional.  According to your code, each item in the list will do something different.

student_ages = [14, 17, 12, 14, 15, 18, 19, 10]

for x in student_ages:

    if x >= 16: 
        print ("this student is old enough to drive")
    else:
        print("this student is not old enough to drive")

# EACH item in the list will be tested to see if it is greater than or equal to
#  In the example above, the print statement "This student is old enough to drive." only runs if x >= 16.   indentation is important.

# RANGE! a list includes all the index spots between two numbers.  The first number is separated from the second number with a colon.
smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies"]

print(smells[2:5])
# The range goes up to the second number after the colon, but does not include it.
#  loops can also be used to run code a certain number of times: for x in range(5): will run 5 times

# UPDATING VARIABLES!  for loops are useful because they can update variables with each loop.  Here is an example of a piece of code that will update the variable named "total" with each loop.
my_list = [2, 5, 8, 10]
total= 0

for x in my_list:
    total= total + x
print(total)

# To create a list of strings, use the following code:
# my_list = input().split() 
# The input should look like words separated by spaces.  No commas, parenthesis, or brackets are needed.

#  may require putting a bunch of numbers as input into a list. To do this, use this code:
# my_list = [int(n) for n in input().split()]
# code creates a list called "my_list" and the input().split() command breaks up the input into each individual integer. It uses a for loop to assign all the individual inputs to their index in the list

# For this code, put your input question right into the input() above.  For example:
#my_list = [int(n) for n in input("Input a list of numbers").split()] 
# The input should look like numbers separated by spaces.  No

# There are several ways to add to a list in python.  One of these methods is append(). 

goats = ['Bili', 'frank', 'bdp']
goats.append('molly')
print(goats)
# adds the value of "Molly" to the end of the list.

# combine lists using the method extend().
goat = ['Bili', 'frank', 'bdp'] 
goat.extend(['Billy', 'bobby', 'brown'])
print (goat)
# This adds the new list to the end of the original list.

goat = ['Bili', 'frank', 'bdp'] 
goat.extend("Fries")
print (goat)
# splits the name into a billion little peices

# Sometimes you might want to add an item to a list in a specific place.  This is done with insert(). use numberes
goat = ['Bili', 'frank', 'bdp'] 
goat.insert(2,"Fries")
print (goat)

# To create a list of strings, use the following code:

my_list = input().split()
# No commas, parentheses, or brackets are needed.

# These challenges may require putting a bunch of numbers as input into a list. To do this, use this code:

my_list = [int(n) for n in input().split()]

# For this code, put your input question right into the input() above.  For example:

my_list = [int(n) for n in input("Input a list of numbers").split()] 

# Removing items from a list can be done with the remove() method.  '
goat = ['Bili', 'frank', 'bdp'] 
goat.('bdp')
print (goat)
# The remove() method will take out the first element that matches.

# Sometimes you will want to actually pull out an item from a list so that it will no longer be in the list, but you still want to use the item value. This is done with the pop() method.
goat = ['Bili', 'frank', 'bdp'] 
favorite = goat.pop(2)
print(favorite + " is my favorite!")
print(goat)

LOOPS!
while True:
    answer = input("Yes or No? ").lower()
    if answer == "yes":
        print("You step out with her, your hand around her shoulder steadying yourself.")
        break  # Exit the loop
    elif answer == "no":
        print("She pulls you out anyway, seeing your disheveled state. You step out with her reluctantly, your hand around her shoulder steadying yourself. “Yeah man, I'm helping whether or not you want it. My name is Joseph. Odd name for a woman so people just call me Jo.”")
        break  # Exit the loop
    else:
        print("Invalid answer, please try again.")

ITERATING LISTS 2D
mylist= [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
rows = 4
cols = 3 

for i in range(rows):
    for j in range(cols):
    mylist[i][j] = mylist[i][j] * 2

print(mylist)
# code that will multiply each element of a 2D list by 2

# access each item in each list that's inside the overall list named my_list. We do this by using range( ).
# additon with strings
my_list = [['dog', 'cat', 'frog'], ['shark', 'squid', 'whale'], ['deer', 'fox', 'badger']]
rows = 3
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] + "is awsome"
        
print(my_list)
# columns are cols
my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]

# Ask the user for the multiplier
multiplier = int(input("Enter a multiplier: "))

# Multiply each element by the multiplier
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        my_list[i][j] = my_list[i][j] * multiplier

# Print the updated list
print(my_list)
# with input

# creating a one dimensional list
n = 5
list = []
for i in range(n):
    list.append(0)
print(list)

# Range to create two d lists
rows = 5
cols = 5
list =[] 
for i in range(cols):
    col= []
    for j in range(rows):
        col.append(i)
    list.append(col)
 # making a list with stuff in it
 # Initialize rows and cols
rows = 4
cols = 3

# Create an empty list
list = []

# Outer loop for rows
for i in range(rows):
    # Inner loop for columns
    row = []  # Create a new row
    for j in range(cols):
        row.append(5)  # Append 5 to the row
    list.append(row)  # Add the row to the list

# Print the resulting list
print(list)

print(list)

# while loops are to print all sigular variables one at a time in a loop.
# for xample
age = 17 

while age >= 0:
    print(age)
    age -= 1
