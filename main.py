# printer(elements)
# - Accepts a list
# - Prints every element of the list
def printer(elements):
    # Your code here
    for i in elements:
        print(i)
    ...


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
def to_celsius(temperatures):
    # Your code here
    new_list = []
    for i in temperatures:
        newI = (i-32)*(5/9)
        new_list.append(newI)
    return new_list

    ...


# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold
def hottest_days(temperatures, threshold):
    # Your code here
    new_list=[]
    for i in temperatures:
        if(i > threshold):
            new_list.append(i)
    return new_list
    ...

# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
def print_hottest_days(temperatures, threshhold):
    # Your code here
    new_list = hottest_days(temperatures,threshhold)
    return to_celsius(new_list)
    ...
