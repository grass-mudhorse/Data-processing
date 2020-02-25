# -*- coding: utf-8 -*-
# Lecture 9 - string manipulation and regular expressions
# This is one of Python's real strengths

# This lecture covers:
# 2nd half of McKinney chapter 7 (string manipulation)
# Regular expressions tutorial at https://docs.python.org/2/howto/regex.html

## String manipulation

# Some revision - here's a simple string
my_string = 'Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed.'
# We can index and slice it just like a list
my_string[3:10]
my_string[-7:]

# We can add and multiply objects with strings:
my_string + ' - ' + 'J'*2 

# Can seperate out into a list by character
list(my_string)

# A quick note on string literals
# If I have something like this:
my_path = 'C:\documents\new'
print(my_path)
# Python will automatically interpret the \n as a new line
# One way of getting round this is to escape the backslashes with 
my_path_2 = 'C:\\documents\\new'
print(my_path_2)
# Another neat way we can get round this by using a string literals
# One example is a raw sting, pre-fixed by r
my_path_3 = r'C:\documents\new'
print(my_path_3)
# Another example is a unicode string (which allows many more characers), prefixed by u - commonly seen in Json objects

# Useful methods for strings:
# splitting
my_string.split(' ') 
my_string.split(',') 
my_string.split() # Removes any whitespace
# Can also specify the number of splits to remove
my_string.split(' ',5)  # splits into 5 by taking the first 4 spaces

# stripping - removes rather than separates but works on individual elements 
# Ususally used via a comprehension
my_string_2 = 'pineapple,  oranges, bananas,  apples'
my_string_3 = [x.strip(' ') for x in my_string_2.split(',')]
# The above separates out by , and then strips out the spaces

# If we have lots of strings to join together we can use join rather than +
', '.join(my_string_3)

# in gives a Boolean as to whether something occurs or not
'Buck' in my_string
'buck' in my_string # Note: case sensitive

# index gives the first location of a ','
my_string.index(',')
my_string.index('Buck') # Note that this is the location of the 'B'
my_string.index('buck') # Gives an error when not found

# an alternative is find which doesn't give an error
my_string.find(',') # Same as index
my_string.find('Buck') # Same as index
my_string.find('buck') # Returns -1

# Count returns the number of times a character or string appears
my_string.count('t')
my_string.count('zzzz') # Gives zero for things not found

# Replace useful for turning one thing into another
my_string.replace('B','D')
my_string.replace('plump','slim')

# endswith and startswith give Boolean
my_string_4 = [x.strip(',. ') for x in my_string.split(' ')] # Get rid of full stops and commas
my_string_4
[x.startswith('a') for x in my_string_4]
[x.endswith('ing') for x in my_string_4]

# Lower and upper convert to upper case
[x.upper() for x in my_string_4]
my_string.lower()

# Some others not covered here - see https://docs.python.org/2/library/stdtypes.html#string-methods
# format: allows you to replace bits inside a string with, e.g. values from a formula
# isalnum: returns true if all the characters are alphanumeric
# isalpha: returns true if all characters are alphabetic
# isdigit: returns true if all characters are numeric
# lstrip and rstrip: strip out only on the left or right hand side
# partition: splits the string into a tuple of three containing the left bit, the split character, and the right bit
# rfind and rindex: do the same as find/index but from the right hand side

################################################################################

# Regular expressions 1

# Regular expressions (regex) are really useful tools for dealing with messy string data
# They are very broad and whole books have been written about using them.
# Unfortunately they are hard to learn and remember, especially if not used regularly
# This section just provides an overview - the McKinney is very poor on regex

# Python has a specific module for dealing with regular expressions. It's called re
# which is already short enough that she doesn't need an alias
import re

# Regular expressions have their own special language. For example \s means a 
# single space and \s+ means at least one space
# This string has some places where there are double spaces, new lines and tab spaces:
hem_string = 'He was an old man who  fished alone in a\n skiff in the  Gulf Stream and he had  gone eighty-four days \tnow without taking a fish.'
print(hem_string)
# Use re.split
re.split('\s',hem_string)
# Compare wtih...
re.split('\s+',hem_string) # Much neater

# We can use other methods too, e.g. findall finds all the specified characters:
re.findall('\s',hem_string)

# Regular expressions in more detail. A key part of regular expressions are 
# 'metacharacters' - here is a list of them:
# . ^ $ * + ? { } [ ] \ | ( )
# They each do special things, and we'll look at them in turn

# First let's look at [ ]. These are used for character classes, for example:
re.findall('[xyz]',hem_string) # Find all the x y or z
re.split('[w-z]',hem_string) # split anywhere there's a w, x, y or z

# Note that sometimes if you include a metacharacter inside a character class it's no longer a metacharacter
re.split('[ab.]',hem_string)

# To find the complement of the set, i.e. the opposite, use ^
re.findall('[^(c-z)]',hem_string) # finds everything that's not between c and z

# To avoid having to write out lots of confusing classes, re has shortcuts:
# \d: match any decimal digits
re.findall('\d',hem_string) # Empty
# \D: match non decimals
re.findall('\D',hem_string) # Everywhere
# \s: whitespace
# \S: Non-whitespace
re.findall('\S',hem_string)
# \w: alphanumeric
# \W: nonalphanumeric
re.findall('\W',hem_string)

# Cleverly you can combine these things, e.g.
# find every whitespace or .
re.findall('[\s,.]',hem_string)

################################################################################

## Regular expressions 2

## Looking for repititions

# A useful metacharacter here is * which means match zero or more of the previous character
# For example ca*t will match ct (i.e. zero a characters), cat (1 a character), caat (2 as), etc
cat_string = 'ct cat cot caat coat cake cate'
re.findall('ca*t',cat_string) # Note that cat is in cate
# A more complicated example is h[a-e]*d. This will match with h at the start, at least 0 of a to e, then ending in d
had_string = 'hd had hed head heed hade heady heaved'
re.findall('h[a-e]*d',had_string) 

# Instead of * (match zero or more times) you can use + which means match 1 or more times
# Notice the differences with the above
cat_string = 'ct cat cot caat coat cake cate'
re.findall('ca+t',cat_string) # Note that cat is in cate
# Or ? which means match exactly zero or once
had_string = 'hd had hed head heed hade heady heaved'
re.findall('h[a-e]?d',had_string) 

# If you want to generalise this you can use {x,y} where x is the min number of 
# repitions you want and y the max number
had_string_2 = 'hd had hed head heed heeed hbbeaccd'
re.findall('h[a-e]{1,2}d',had_string_2) # Match exactly once or twice
# Look at how complicated we've got already!

# We can combine character classes to create more complicated regular expressions
# Suppose we wanted to find all of the words for which the first letter was 
# capitalised
re.findall('[A-Z][a-z]*',hem_string)
# This will find all words with exactlt one capital letter, followed by any number
# of lowercase letters
# We can also combine digits, special characters and letters.
my_string_5 = 'The material for this week is in section 7.3 of the McKinney book, which starts on page 215, table 7-3 on page 217 lists some of the built-in string methods for Python.' 
re.findall('[a-z]+\s\d+[-.]?\d*',my_string_5)
# Can you figure out this regular expression?

## Using regular expressions
# This isn't always quite as simple as the above as re doesn't always give you
# what you'd expect

# Perhaps the best way to use re (at least if you're doing this often) is to
#'compile' the command and re-use it
my_regex = re.compile('\s+')
my_regex.split(hem_string)
my_regex.split(my_string)
# This compiling makes code run much faster as otherwise each individual command
# needs to be compiled again within re

# Note that my_regex can be printed out to remind us what it is
my_regex
# Tell us what type of object it is
print(my_regex)

# To make .compile a bit richer, you can add flags:
my_regex_2 = re.compile('[a-z]+ee[a-z]+',flags=re.IGNORECASE)
# This will ignore the case in when searching for regular expressions that match
# '[a-z]+ee[a-z]+'
# Testing it out on the string below
seuss_string = 'And will you succeed? Yes you will INDEED! (98 and 3/4 percent Guaranteed.)'
my_regex_2.findall(seuss_string)
# This returns all of the words with ee in them, regardless of the case of the 
# word/letters in the word.
# Another useful flag is MULTILINE, which matches things at the beginning 
# (and/or end) of each line within the string


# What else can you do with a regular expression?
# We're going to look at match and search

# Match sees whether the re matches at the beginning of the string
# Search looks for all substrings where the re matches

# Let's try a very simple expression
simple_re = re.compile('[a-z]+') # so does the string contain at least one of a to z
simple_re.search('54321 hello!') # Doesn't give me anything useful!
# It's actually better to store this in an object and then use methods on that object
h = simple_re.search('54321 hello!')
# Look at group: shows all the accepted bits
h.group() 
# Start shows where the search starts
h.start()
# end shows where the search ends
h.end()
# span shows both in a tuple
h.span()

# Notice the difference if I had called match instead
m = simple_re.match('54321 hello!')
# Should give errors now because it couldn't find it at the start; m is empty
m.group()
# This means you'd commonly check whether m was None or not before doing anything with it

################################################################################

## Regular expressions 3

# More metacharacters

# The verical pipe | is the or operator so a|b matches a or b
# Be careful because bat|man matches bat or man, not baman or batan
bat_string = 'batman baman batan'
re.findall('bat|man',bat_string)

# Use ^ to match at the beginning of lines
super_heroes = 'superman batman spiderman hulk ironman'
re.findall('^s',super_heroes) #start with s?
re.findall('^b',super_heroes) #start with b?
# This second one finds nothing because ^ only looks at the start of the string
# Use with multiline or in a comprehension for looking within strings
[re.findall('^b',x) for x in super_heroes.split()]

# Use $ to match at the end of a string
re.findall('man$',super_heroes)
[re.findall('man$',x) for x in super_heroes.split()]

# Use \b to match a word boundary
re.findall(r'\bStream\b',hem_string) # Stream is there
re.findall(r'\bream\b',hem_string) # ream is not
# Notice that i'm using raw string literals here, otherwise Python interprates 
# \b as the backspace character

# Grouping - use () in the same way you would in a mathematical expression
# e.g. (rm)+ means match at least one of pattern rm, different from r(m+)
re.findall('(rm)+',super_heroes)
re.findall('r(m+)',super_heroes) # Find a match of r followed by at least one of m
# You can do much more complicated things with () - see the tutorial

# Finally sub and subn
# sub changes a pattern into something else specified by replacement
re.sub('super|man','lex_luther',super_heroes)
# Replace super or man with lex_luther

# subn does the same thing but tells you how many replacements it made
re.subn('super|man','lex_luther',super_heroes) # 5 replacement
# Returns a 2-tuple

# If there's no match just returns the original string
re.sub('cat|woman','bruce_wayne',super_heroes)

# These can also be compiled as before

# A few words of caution to finish off
# Don't use sub unless you actually need a re, otherwise just use replace
# Be careful with escape characters mixing up with metacharacters
# Remember the difference between match and search
# Lots more things not covered here - see more of the tutorial, or google Python regular expressions




