# -*- coding: utf-8 -*-
# Week 2 - Assessed exercises
import math
# Q1 Write a for loop to compute the sum of x^2 for x from 0 to 8. What is the
# value of this sum?
sum = 0
for x in range(9):
    sum += x*x
print(sum)
# Ans: 204

# Q2 Define a function (addition) that returns the sum of two numbers x and y.
# Use the function to calculate 2.09 + 8.73
def addition(x,y):
    n_sum = x + y
    return n_sum

print(addition(2.09,8.73))
# Ans: 10.82

# Q3 Find the 3 errors in the code below. The function sin_estimate should
# calculate an estimate of the sine function at the value 'x', with an error
# tolerance of 'tol'. After finding the 3 errors and fixing the code, the
# variable y should equal 0.09983341666666667
def sin_estimate(x,tol=10**-10):
    sin_est = 0
    i = 0
    error = abs(sin_est-math.sin(x))
    while error > tol and i<50:
        sin_est += ((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1)
        error = abs(sin_est-math.sin(x))
        i += 3 
    return sin_est
y = sin_estimate(0.1)
print(y)                 
# Ans: 
# Error 1 = Missing a colon when create the function. 
# Error 2 = Did not import "math" package and write the worong format when using sin(x) function.
# Error 3 = Forget to add the return value.

# Q4 A bakery sells cupcakes, cookies and pastries. A cupcake costs €1.50, a 
# cookie costs €1.00 and a pastry costs €0.80. However, the bakery offers 
# discounts if you buy multiple items. If you buy 4-8 cupcakes they cost €1.20 
# each, and if you buy more then 8 they are €1.00 each. If you buy 5 or more 
# cookies they are €0.80. If you buy more than 3 pastries they are reduced to 
# €0.65 each, and reduced further to €0.50 if you buy 10 or more.
# Create a set of nested if/elif/else statements to determine the price of each
# item based on the amount the customer requests and then computes the total
# cost of the order.
# Pay attention to the phrasing "more than n", "n or more" one includes the 
# value 'n' and the other does not.
# Use your code to determine the total cost of 8 cupcakes, 4 cookies and 12 
# pastries.
def cost_total(num_cupcake,num_cookie,num_pastry):
    cost_cupcake = 0
    cost_cookie = 0
    cost_pastry = 0
    cost_total = 0
    
    if num_cupcake in range(0,4):
        cost_cupcake = num_cupcake*1.50
    elif num_cupcake in range(4,9):
        cost_cupcake = num_cupcake*1.20
    else:
        cost_cupcake = num_cupcake*1.00
    
    if num_cookie in range(0,5):
        cost_cookie = num_cookie*1.00
    else:
        cost_cookie = num_cookie*0.80
    
    if num_pastry in range(0,4):
        cost_pastry = num_pastry*0.80
    elif num_pastry in range(4,10):
        cost_pastry = num_pastry*0.65
    else:
        cost_pastry = num_pastry*0.5
    
    cost_total = cost_cupcake + cost_cookie + cost_pastry
    return cost_total

print(cost_total(8,4,12))
# Ans: the total cost of desserts is 19.60 euro.
