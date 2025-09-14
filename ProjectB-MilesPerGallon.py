# Project B
# Program 1, calculate Miles per gallon
# wil prompt user for input

print(' This program Calculates Miles per Gallon : ')

# Ask input from the user

miles_driven = input(" Enter the miles driven ")

# convert text entered to a Float point number

miles_driven = float ( miles_driven)

# Get the gallon used from the user

gallons_used = input(" Enter Gallon Used : " )
cost_of_gallon=float(input(' Enter the cost of Galllon in Dollar : '))

# Convert  text entered to a float point number

gallons_used = float(gallons_used)

# Calculate and print the answer

mpg = miles_driven / gallons_used

print(' MIles per Gallon  : ', mpg)

cost_of_trip = mpg * cost_of_gallon

print(' Cost of the Trip in USD is : ', cost_of_trip)



