# -*- coding: utf-8 -*-
"""temp_analyzer.py

"""
# Python libraries are not required for this Exercise, but if you do load any libraries, do so before the dataset
# This file should contain all your Python code, including functions


# tempData list has 336 integers in the list.  In later assignments we will load an external 
# datafile (e.g. .txt or .csv), but as this dataset is not very large, we'll place the data directly in the Python code
# List of half-hourly temperature values (in degrees Fahrenheit) for one week
tempData =  [19, 21, 21, 21, 23, 23, 23, 21, 19, 21, 19, 21, 23, 27, 27, 28, 30, 30, 32, 32, 32, 32, 34, 34,
             34, 36, 36, 36, 36, 36, 36, 34, 34, 34, 34, 34, 34, 32, 30, 30, 30, 28, 28, 27, 27, 27, 23, 23,
             21, 21, 21, 19, 19, 19, 18, 18, 21, 27, 28, 30, 32, 34, 36, 37, 37, 37, 39, 39, 39, 39, 39, 39,
             41, 41, 41, 41, 41, 39, 39, 37, 37, 36, 36, 34, 34, 32, 30, 30, 28, 27, 27, 25, 23, 23, 21, 21,
             19, 19, 19, 18, 18, 18, 21, 25, 27, 28, 34, 34, 41, 37, 37, 39, 39, 39, 39, 41, 41, 39, 39, 39,
             39, 39, 41, 39, 39, 39, 37, 36, 34, 32, 28, 28, 27, 25, 25, 25, 23, 23, 23, 23, 21, 21, 21, 21,
             19, 21, 19, 21, 21, 19, 21, 27, 28, 32, 36, 36, 37, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 41,
             41, 41, 41, 39, 37, 36, 36, 34, 32, 30, 28, 28, 27, 27, 25, 25, 23, 23, 23, 21, 21, 21, 19, 19,
             19, 19, 19, 19, 21, 23, 23, 23, 25, 27, 30, 36, 37, 37, 39, 39, 41, 41, 41, 39, 39, 41, 43, 43,
             43, 43, 43, 43, 43, 43, 43, 39, 37, 37, 37, 36, 36, 36, 36, 34, 32, 32, 32, 32, 30, 30, 28, 28,
             28, 27, 27, 27, 27, 25, 27, 27, 27, 28, 28, 28, 30, 32, 32, 32, 34, 34, 36, 36, 36, 37, 37, 37,
             37, 37, 37, 37, 37, 37, 36, 34, 30, 30, 27, 27, 25, 25, 23, 21, 21, 21, 21, 19, 19, 19, 19, 19,
             18, 18, 18, 18, 18, 19, 23, 27, 30, 32, 32, 32, 32, 32, 32, 34, 34, 34, 34, 34, 36, 36, 36, 36,
             36, 32, 32, 32, 32, 32, 32, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 28, 28]

# Begin your functions and code here, do not forget to document your code with comments
def fahrenheit_to_celsius(temp_fahrenheit:float)->float:
    """
    Part 1
    ---

    This function converts a temperature in Fahrenheit to Celsius.

    How to use the function:
    ```python 
    temperature_fahrenheit = 32
    temp_celsius = fahrenheit_to_celsius(temperature_fahrenheit)

    print(temp_celsius)
    # prints 0.0
    ```

    Parameters
    ----------
    temp_fahrenheit : float
        Temperature in Fahrenheit
    
    Returns
    -------
    float
        Temperature in Celsius
    """
    converted_temp = (temp_fahrenheit - 32) / 1.8
    return converted_temp

def temperature_classifier(temperature_celsius:float)-> int:
    """
    Classify the temperature in Celsius into categories.

    Parameters
    ----------
    temperature_celsius : float
        Temperature in Celsius.

    Returns
    -------
    int
        Classification category:
        - 0: temperatures below -2 degrees Celsius
        - 1: temperatures from -2 up to +2 degrees Celsius
        - 2: temperatures from +2 up to +15 degrees Celsius
        - 3: temperatures above +15 degrees Celsius

    Examples
    --------
    >>> temperature_classifier(-5)
    0
    >>> temperature_classifier(0)
    1
    >>> temperature_classifier(10)
    2
    >>> temperature_classifier(20)
    3
    """
    if temperature_celsius < -2:
        return 0
    elif temperature_celsius >= -2 and temperature_celsius < 2:
        return 1
    elif temperature_celsius >= 2 and temperature_celsius < 15:
        return 2
    elif temperature_celsius >= 15:
        return 3
classes_meaning = {
    0:"Cold",
    1:"Slippery",
    2:"Comfortable",
    3:"Warm",
}
temp_classes = [ ]
temp_classification = {
    "temp":[],
    "classification":[],
}
for temp_f in tempData:
    temp_celsius = fahrenheit_to_celsius(temp_f)
    temp_class = temperature_classifier(temp_celsius)
    temp_classes.append(temp_class)

    # using a dictionary
    temp_classification["temp"].append(round(temp_celsius))
    temp_classification["classification"].append((classes_meaning[temp_class]))

# NOTE: How many temperatures are there within each temperature class?
# using list
for i in range(0,4):
    print("Count for {} temperature, class {}: {}".format(classes_meaning[i],i, temp_classes.count(i)))
# Results
# Count for Cold temperature, class 0: 137
# Count for Slippery temperature, class 1: 85
# Count for Comfortable temperature, class 2: 114
# Count for Warm temperature, class 3: 0