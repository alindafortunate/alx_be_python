def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):

    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 // 5
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temperature = float(input("Enter the temperature to convert: "))
question = (
    input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().capitalize()
)
if question == "F":
    print(f"{temperature}°C is {convert_to_celsius(temperature)}°F")
elif question == "C":
    print(f"{temperature}°F is {convert_to_fahrenheit(temperature)}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")
