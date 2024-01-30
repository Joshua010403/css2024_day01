# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:44:03 2024

@author: Joshua van Zyl
"""

# 4. Storing Data in Python

"""
    1. Lists
    2.Dictionaries
    3. Data Frames
"""

# 0. General

# Storing Data
"""
age1 = 30
age2 = 40
age3 = 30
age4 = 49
age5 = 22
age6 = 35
age7 = 22
age8 = 46
age9 = 29
age10 = 25
age11 = 39

print(age1)
print(age2)
print(age3)
print(age4)
print(age5)
print(age6)
print(age7)
print(age8)
print(age9)
print(age10)
print(age11)


# Using Lists

age = [30,40,30,49,22,35,22,46,29,25,39]

print(age)

# List indexes start at 0 

print(age[0])
print(age[1])
print(age[10])

# Going out of list bounds will cause an error

# print(age[11])
"""

# Basic Stats

age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

print(age[0:2]) # Will be value in list minus one, i.e. how many indexes to show

age.append(100) # Append values to a list

print("\n")

# Storing Text

"""
C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)


# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
"""

# gender list

gender = ["M","M","F","M","F","F","F","M","M","F","M"]

print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])
print("\n")

# country list

country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])
print("\n")


# 1. Lists

# Data Storage With Lists

my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)

print(my_list[:])
my_list.append('appended')
my_list.insert(0,"inserted")
my_list.remove("inserted")
print(age[0:2]) # Will be value in list minus one, i.e. how many indexes to show
print("\n")


#2. Dictionaries

"""
Dictionaries - key:value pairs

cat: "a selfish animal"
"""

mammals = {"cat":"a selfish animal","lion":"big kitty","elephant":"not a kitty"}

print(mammals["cat"])
print("\n")

# 3. Data Frames

"""
Data Frames
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

sizes_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
        
    "fruits": fruits,
    "sizes": sizes_nm
    }

"""
df = dataframe
"""

import pandas as pd

df = pd.DataFrame(fruit_sizes)

print(df["fruits"])
print(df["sizes"])

print(df["sizes"].min())
print(df["sizes"].mean())

print(df.describe())

print(df[ df["sizes"] > 10 ])   # Filtering in Data Frames

print(df[1:3])

# Adding or removing a column of data

prices = [10.00, 12.5, 16.00, 23.00, 7.00]

df["prices"] = prices

df.drop(columns=["sizes"], inplace=True)
