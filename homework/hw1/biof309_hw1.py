"""
biof309_hw1.py

Written by Chris Coletta

The purpose of this script is to test if you have properly installed Python 2.7 and NumPy

The script will promt the user for his or her last name, and transform it into a single,
reproducible number which can be emailed to the instructor for verification.
"""


# Step 1: Import all the packages we'll need to do what we want to do
# The following 3 are core packages that come with Python
import hashlib
import string
import math

# This one is a package that must be installed separately
# NumPy is a popular matrix math package that we will use extensively throught the semester
import numpy



# Step 2: Get input from the user, and capitalize their name, all in one step
name = raw_input( "please enter your last name =========> " ).capitalize() 
print "\n\n\n" # Skip three lines
print "Your name, properly capitalized, is this: ", name




# Step 3: Convert the user input into a predictable series of numbers and letters
# For more information look up "Cryptographic hash function"
string_of_letters_and_numbers = hashlib.sha224(name).hexdigest()
print "The cryptographic hash value associated with your name: ", string_of_letters_and_numbers





# Step 4: Strip out all the letters, leaving only numbers
just_the_numbers = string_of_letters_and_numbers.translate( None, string.letters )
print "With all the letters stripped out: ", just_the_numbers
# Now we convert the string of numeric characters into a list of integers
list_of_numbers = [ int( digit ) for digit in list( just_the_numbers ) ] 




# Step 5: Resize the numbers into a square NumPy matrix

# How many numbers do we have?
number_of_numbers = len( list_of_numbers )
# Take the square root
square_root =  math.sqrt( number_of_numbers )
# Lop off the decimal, leaving only the integer
square_root_integer = int( square_root )
# Load the numbers into a 1 X N matrix
flat_matrix = numpy.array( list_of_numbers )
# resize the matrix into a square matrix
square_matrix = numpy.resize( flat_matrix, ( square_root_integer, square_root_integer) )
print "Those numbers, resized into a {} by {} matrix:".format( square_root_integer, square_root_integer )
print square_matrix



# Step 6: Calculate the determinant of the matrix and output, which is the magic number.
determinant = numpy.linalg.det( square_matrix )
print "The determinant of that matrix (your magic number): ", determinant

print "Congratulations, your Python environment is configured properly!!\n\n"

print 'Write an email to christopher.coletta@gmail.com, subject line: "{} {}"'.format( name, determinant )
print "and put something entertaining/interesting in the body of the email for me to read and enjoy."
