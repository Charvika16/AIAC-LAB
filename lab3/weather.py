def weather_condition(temperature):
    if temperature > 30:
        return "hot"
    elif 15 <= temperature <= 30:
        return "warm"
    else:
        return "cold"
#example usage
print(weather_condition(25)) # Output: warm
print(weather_condition(35)) # Output: hot
print(weather_condition(10)) # Output: cold
print(weather_condition(15)) # Output: warm
print(weather_condition(30)) # Output: warm