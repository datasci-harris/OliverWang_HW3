# Oliver Wang (Su Wang)
# suwang26
# oliverwang266

"""
INSTRUCTIONS

Available: May 2nd

Due: May 12th at 11:59PM

Gentle reminder that, among other things, you

(a) Must answer your questions in the homework3.py file
(b) Must homework3.py commit to your clone of the GitHub homework repo
(c) Must link your GitHub repo to GradeScope
(d) Must NOT repeatedly use a hard-coded path for the working directory
(e) Must NOT modify the original data in any way

Failure to do any of these will result in the loss of points
"""

"""
QUESTION 1

In this question, you'll be replicating the graph from Lecture 14, slide 5
which shows the population of Europe from 0 AD to the present day in both
the linear and the log scale. You can find the data in population.csv, and the
variable names are self-explanatory.

Open this data and replicate the graph. 

Clarification: You are not required to replicate the y-axis of the right hand
side graph; leaving it as log values is fine!

Clarification: You are not required to save the figure

Hints: Note that...

- The numpy function .log() can be used to convert a column into logs
- It is a single figure with two subplots, one on the left and the other on
the right
- The graph only covers the period after 0 AD
- The graph only covers Europe
- The figure in the slides is 11 inches by 6 inches
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

# Load the data
data = pd.read_csv('population.csv')

# Filter data for Europe and years after 0 AD
data = data[(data['Entity'] == 'Europe') & (data['Year'] >= 0)]

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 6))

# Linear scale plot
ax1.plot(data['Year'], data['Population (historical estimates)'])
ax1.set_title('Population of Europe (Linear Scale)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Population')

# Log scale plot
ax2.plot(data['Year'], np.log(data['Population (historical estimates)']))
ax2.set_title('Population of Europe (Log Scale)')
ax2.set_xlabel('Year')
ax2.set_ylabel('Log of Population')

plt.show()
"""
QUESTION 2

A country's "capital stock" is the value of its' physical capital, which includes the 
stock of equipment, buildings, and other durable goods used in the production 
of goods and services. Macroeconomists seem to conisder it important to have 
public policies that encourage the growth of capital stock. Why is that?

In this exercise we will look at the relationship between capital stock and 
GDP. You can find data from the IMF in "capitalstock.csv" and documentation in
"capitalstock documentation.txt".

In this exercise we will only be using the variables that are demarcated in
thousands of 2017 international dollars to adjust for variation in the value 
of nominal national currency. Hint: These are the the variables that 
end in _rppp.

1. Open the dataset capitalstock.csv and limit the dataframe to only 
observations from 2018

2. Construct a variable called "capital_stock" that is the sum of the general
government capital stock and private capital stock. Drop 
observations where the value of capital stock is 0 or missing. (We will be 
ignoring public-private partnership capital stock for the purpose of t
his exercise.)

3. Create a scatterplot showing the relationship between log GDP and log
capital stock. Put capital stock on the y-axis. Add the line of best 
fit. Add labels where appropriate and make any cosmetic adjustments you want.

(Note: Does this graph suggest that macroeconomists are correct to consider 
 capital stock important? You don't have to answer this question - it's 
 merely for your own edification.)

4. Estimate a model of the relationship between the log of GDP 
and the log of capital stock using OLS. GDP is the dependent 
variable. Print a table showing the details of your model and, using comments, 
interpret the coefficient on capital stock. 

Hint: when using the scatter() method that belongs to axes objects, the alpha
option can be used to make the markers transparent. s is the option that
controls size
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

# Load the data
data = pd.read_csv('capitalstock.csv')

# Filter the data for 2018 and relevant columns
data = data[data['year'] == 2018]

# Creating 'capital_stock' variable by summing general and private capital stock
data['capital_stock'] = data['kgov_rppp'] + data['kpriv_rppp']

# Drop rows where capital_stock is 0 or missing
data.dropna(subset=['capital_stock', 'GDP_rppp'], inplace=True)
data = data[data['capital_stock'] > 0]

# Creating the scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(np.log(data['capital_stock']), np.log(data['GDP_rppp']), alpha=0.5, s=50)
plt.title('Relationship between Log GDP and Log Capital Stock')
plt.xlabel('Log Capital Stock')
plt.ylabel('Log GDP')
plt.grid(True)

# Adding line of best fit
x = sm.add_constant(np.log(data['capital_stock']))
model = sm.OLS(np.log(data['GDP_rppp']), x)
results = model.fit()
plt.plot(np.log(data['capital_stock']), results.predict(x), color='red')

# Show the plot
plt.show()

# Print the summary of the OLS model
print(results.summary())
