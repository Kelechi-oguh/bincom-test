import psycopg2
import numpy as np
import pandas as pd
from collections import Counter
from statistics import variance


data = {
    'MONDAY': [
        'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'
        ],
    'TUESDAY': [
        'ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'
    ],
    'WEDNESDAY': [
        'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'
    ],
    'THURSDAY': [
        'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'
    ],
    'FRIDAY': [
        'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE'
    ]
}

colour_list = []


for key, values in data.items():
    for colour in values:
        colour_list.append(colour)

colour_count = Counter(colour_list)

new_data = pd.Series(colour_count)
print('New Data: ', new_data, '\n')


# The Mean
print('The Mean: ', new_data.mean(), '\n')

# Which color is mostly worn throughout the week?
the_mode = new_data.max()
mode_colour = new_data[new_data==the_mode]
print('The Mostly Worn Colour: ', mode_colour, '\n')

# The Median
print('The Median: ', new_data.median(), '\n')

# The Variance
print('The Variance: ', variance(new_data), '\n')


# Probability that a color is red:
pr_red = new_data.sum() / new_data['RED']
print('Probability of choosing RED: ', pr_red, '\n')



# Save the colours and their frequencies in postgresql database
# try:
#     # establish connection
#     conn = psycopg2.connect(
#         host='localhost',
#         database="db",
#         user='db',
#         password='db',
#         port= '5432'
#     )
    
#     conn.autocommit = True
    
#     # Creating a cursor object
#     cursor = conn.cursor()
    
#     # Doping EMPLOYEE table if already exists.
#     cursor.execute("DROP TABLE IF EXISTS dress_colour")

#     # create table
#     table ='''CREATE TABLE dress_colour(colour VARCHAR(255) NOT NULL, frequency INT)'''
#     cursor.execute(table)

#     insert_query = """ INSERT INTO dress_colour(colour, frequency) VALUES (%s,%s)"""
#     for key, value in colour_count.items():
#         cursor.execute(insert_query, (key, value))

# except (Exception, psycopg2.Error) as error:
#     print("Failed to insert record into publisher table", error)
 
# finally:
#     # closing database connection.
#     if conn:
#         cursor.close()
#         conn.close()
#         print("PostgreSQL connection is closed")



# A recursive searching algorithm to search for a number entered by user in a list of numbers.
def search(arr, num, startIndex, endIndex):
    # Ensure the list is sorted in ascending/descending order for the function to work correctly
    if endIndex >= startIndex:
 
        midIndex = (endIndex + startIndex) // 2 # The middle Index of the array
 
        # If the number is present at the middle
        if arr[midIndex] == num:
            return midIndex
 
        # If number is not in middle, then;
        elif arr[midIndex] > num:
            return search(arr, num, startIndex, midIndex - 1)
 
        else:
            return search(arr, num, midIndex + 1, endIndex)
 
    else:
        # number is not present in the array
        return -1
    

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 3

result = search(arr, num, 0, len(arr)-1)

# To test the search function
# if result != -1:
#     print("Number is present at index", str(result), '\n')
# else:
#     print("Number not found in array", '\n')


# Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
rand_n = np.random.randint(0, 2, size=(1,4))[0]
numb = ''
for i in rand_n:
    numb = numb + str(i)

print('Binary number: ', numb)

to_base10 = int(numb, 2)
print('to_base10: ', to_base10, '\n')


# Write a program to sum the first 50 fibonacci sequence.
def fibonacci_Sum(n) :
    if (n <= 0) :
        return 0
  
    fib =[0] * (n+1)
    fib[1] = 1
  
    # Initialize result
    fib_sum = fib[0] + fib[1]
  
    # Add remaining terms
    for i in range(2, n+1) :
        fib[i] = fib[i-1] + fib[i-2]
        fib_sum = fib_sum + fib[i]
         
    return fib_sum

print('Sum of first 50 Fibonacci Numbers: ', fibonacci_Sum(50))
