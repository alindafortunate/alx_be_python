# A  program about current weather conditions.
weather_today = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather_today == "sunny":
    print(f"Wear a t-shirt and sunglasses.")
elif weather_today == "rainy":
    print(f"Don't forget your umbrella and a raincoat.")
elif weather_today == "cold":
    print(f"Make sure to wear a warm coat and a scarf.")
else:
    print(f"Sorry, I don't have recommendations for this weather.")
