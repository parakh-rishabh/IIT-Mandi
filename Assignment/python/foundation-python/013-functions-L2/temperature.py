# Temperature Conversion

# Write two functions named celsiusToFahrenheit and fahrenheitToCelsius to convert between Celsius and Fahrenheit.

# Use the functions to convert a given temperature.
# (0°C × 9/5) + 32 = 32°F
import math
def celsius_To_Fahrenheit(celcius):
    far=(celcius*9/5)+32
    return far
def fahrenheit_To_Celsius(fahrenheit):
    cel=(fahrenheit-32)*5/9
    return cel
fer=celsius_To_Fahrenheit(27)
print(round(fer,2))
cel=fahrenheit_To_Celsius(76)
print(round(cel,2))




     