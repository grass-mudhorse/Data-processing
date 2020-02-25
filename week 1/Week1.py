# Week 1 - Assessed Exercises
# Fill in the following Python script and submit it on Brightspace.
# An empty line between the question and 'Ans:' implies that you will need to 
# write a piece of code to get the answer.
import pandas as pd
import numpy
# Import Heart Disease UCI data set and call is heart
heart = pd.read_csv('E:\semester 1\data pro\week 1\heart.csv')

# Q1 (a) How many rows and columns there are in the Heart Disease UCI data set?
print(heart)
# Ans: This data set has 303 rows and 14 columns. 


# Q1 (b) What sex is the 3rd person in the data set, i.e. on the third row?
print(heart.loc[2].sex)
# Ans: The gender of the 3rd person is female (sex value is 0).


# Compute the table of different chest pain types. 

# Q2 How many people have type 3 chest pain? 
print(heart.cp.value_counts())
# Ans: The number of people have type 3 chest pain is 23.

# Q3 (a) What age is the youngest person in this dataset? 
print(heart.age.min())
# Ans: The youngest age is 29.


# Q3 (b) What age is the oldest person in this dataset? 
print(heart.age.max())
# Ans: The oldest age is 77.

# Look up what the cut function (pd.cut) does and use it to create a new 
# variable which is age grouped into 20-30, 30-40, 40-50, 50-60, 60-70, 70-80. 
bins = [20,30,40,50,60,70,80]
heart['age_groups'] = pd.cut(heart.age, bins = bins, right = False)
groups = heart['age_groups']
print(groups)

# Q4 How many people are in the group (50,60)? 
print(groups.value_counts())
# Ans: 125 people are in group (50,60) (including the age of 50, but not 60).




