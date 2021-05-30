#!/usr/bin/env python
# coding: utf-8

# ## Problem 2 - Plotting temperatures 
# 
# In this problem we will  plot monthly mean temperatures from the Helsinki-Vantaa airpot for the past 30 years.
# 
# ## Input data
# 
# File c monthly average temperatures from Helsinki Vantaa airport. Column descriptions:
# 
# ### Part 1
# 
# Load the Helsinki temperature data (`data/helsinki-vantaa.csv`)
# 
# - Read the data into variable called `data` using pandas
# - Parse dates from the column `'DATE'` and set the dates as index in the dataframe 

# YOUR CODE HERE 1 to read the data into data and parse dates

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#create file path
fp = 'data/helsinki-vantaa.csv'
#load the data and parse dates
data = pd.read_csv(
  fp, 
  parse_dates=['DATE'], index_col=['DATE']
)

# This test print should print first five rows
print(data.head())

# Check the number of rows in the data frame
print(len(data))

# ### Part 2
# 
# Select data for a 30 year period (January 1988 - December 2018)
# 
# - Store the selection in a new variable `selection`

# YOUR CODE HERE 2
# select data for a 30 year period and store the variable 'selection'
selection = data.loc['1988-01-01':'2018-12-31']
#data[(data['DATE'] > datetime(1988, 1, 1)) & (data['DATE'] < datetime(2018, 12, 31))]
#
#

# Check that the data was read in correctly:
selection.head()

# Check how many rows of data you selected:
print("Number of rows:", len(selection))

# ### Part 3
# 
# #### Part 3.1
# 
# Create a line plot that displays the temperatures (`TEMP_C`) for yeach month in the 30 year time period:
#      
# #### Part 3.2
# 
# Save your figure as PNG file called `temp_line_plot.png`.
# 

# YOUR CODE HERE 3
#plot the selection["TEMP_C"] 
ax = selection['TEMP_C'].plot(
  figsize=(20, 6), # set the size
  color='black', marker='.', #markers are black dots.
  title = "Helsinki-Vantaa Airport", #add title
  linestyle='solid', 
  xlabel='Time', ylabel='Temperature(Celsius)' #add x and y label
)
# add grid line
plt.grid()

# Set output file name
outputfp = "" 

# Save plot as image
# YOUR CODE HERE 4
outputfp = "temp_line_plot.png"
plt.savefig(outputfp)

import os

#Check that output file exists (also open the file and check that the plot looks ok!)
os.path.exists(outputfp)

# **REMINDER**: Don't forget to upload your figure and the modified notebook into your personal GitHub repository!
# 
# ### Done!
