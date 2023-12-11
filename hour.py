def convert_to_24hrs(hour, minute, period):
    # Changing the hour based on the period
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    # Changing the format into 24hr form
    result = "{:02d}{:02d}".format(hour, minute)
    return result

# results
print(convert_to_24hrs(10, 50, "am"))  # Output will be 1050
print(convert_to_24hrs(10, 50, "pm"))  # Output will be 2250
print(convert_to_24hrs(12, 45, "am"))  # Output will be 0045
print(convert_to_24hrs(12, 45, "pm"))  # Output will be 1245
print(convert_to_24hrs(1, 20, "am"))   # Output will be 0120
print(convert_to_24hrs(1, 20, "pm"))   # Output will be 1320
