CELSIUS_TO_FAHRENHEIT_FACTOR = 9 // 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR

    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    temperature = float(input("Enter the temperature to convert: "))
    question = (
        input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        .strip()
        .capitalize()
    )
    if question == "F":
        print(f"{temperature}°C is {convert_to_celsius(temperature)}°F")
    elif question == "C":
        print(f"{temperature}°F is {convert_to_fahrenheit(temperature)}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
