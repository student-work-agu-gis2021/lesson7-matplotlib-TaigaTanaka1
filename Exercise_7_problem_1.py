#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: Simple scatter plot using random 
# 
# We can generate random numbers using using a method `random.rand()` from the [NumPy package](https://numpy.org/). This example generates 10 random values:
# 
# ```
# import numpy as np
# random_numbers = np.random.rand(10)
# 
# ```
# 
# ### Part 1
# 
# Create an new data frame called `data` and add 1000 random numbers (`float`) into a new column `x` and another 1000 random numbers (`float`) into a new column `y`.

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
from matplotlib import cm

# YOUR CODE HERE 1 to set data
#create the data and add 1000 random numbers into each columns.
data = pd.DataFrame(np.random.rand(2000).reshape(1000,2), columns = ['x','y'])

# Check your random values
print(data.head())

# Check that you have the correct number of rows
assert len(data) == 1000, "There should be 1000 rows of data."


# ### Part 2
# 

# YOUR CODE HERE 2 to set colors
#create 1000 random numbers.
colors = np.random.rand(1000)

# This test print should print out 10 first numbers in the variable colors
print(colors[0:10])

# Check that the length matches
assert len(colors) == 1000, "There should be 1000 random numbers for colors"


# ### Part 3 
# 
# #### Part 3.1
# 
# Create a scatter plot of points with random colors
# 
# #### Part 3.2
# 
# #### Part 3.3
# 

# Plot a scatter plot
# YOUR CODE HERE 3
#scatter plot. 
#use 'Accent' for colormap. edgecolor is black. size is 100
ax = plt.scatter(
  data['x'], data['y'],
  cmap=cm.Accent,
  s=100, c=colors,
  edgecolor="black"
  )
plt.colorbar()

# Add labels and title
# YOUR CODE HERE 4
# create variable title, xlabel and ylabel, for a nice plot
title = "My random candy points"
xlabel = "X-label"
ylabel = "Y-label"
#add these labels for a graph
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
# Save the plot as a png file:
outputfp = "my_first_plot.png"

# YOUR CODE HERE 5
plt.savefig(outputfp)
# This test print statement should print the output filename of your figure
print("Saved my first plot as:", outputfp)

#Check that the file exists (also go and open the file to check that everything is ok!)
import os

assert os.path.exists(outputfp), "Can't find the output image."


# Remember to commit your changes (including the image file) to your GitHub repo!
# 
# ### Done!
# 
# Now you can move to [problem 2](Exercise-7-problem-2.ipynb).
