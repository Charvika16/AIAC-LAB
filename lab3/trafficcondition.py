def traffic_condition(traffic):
    if traffic > 50:
        return "heavy"
    elif 20 <= traffic <= 50:
        return "moderate"
    else:
        return "light"
#example usage
print(traffic_condition(10)) # Output: light
print(traffic_condition(30)) # Output: moderate
print(traffic_condition(60)) # Output: heavy
print(traffic_condition(20)) # Output: moderate