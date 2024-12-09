"""
Simple Temperature Conversion Functions
Author: Franklin Rodriguez
Date: 2024-10-21
"""
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

if __name__ == "__main__":
    # NOTE: testing functions
    # Test 1:
    print(fahrenheit_to_celsius(48)) # prints 8.88888888888889
    # Test 2:
    print(fahrenheit_to_celsius(71)) # prints 21.666666666666668

    # NOTE: testing temperature_classifier function
    temperatures_in_f = [32, 50, -10, 80]
    # Convert temperatures to celsius
    temperatures_in_c = [fahrenheit_to_celsius(temp) for temp in temperatures_in_f]
    # get category for the temperatures in celsius
    # the line of code below creates a dictionary with temperature as the key
    # and its respective class
    categories = {temp:temperature_classifier(temp) for temp in temperatures_in_c}
    # prints {0.0: 1, 10.0: 2, -23.333333333333332: 0, 26.666666666666664: 3}
    print(categories)



