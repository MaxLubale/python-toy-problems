def convert_to_24_hour_format(hour, minute, period):
    if period.lower() == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    # Format the hour and minute as two-digit strings
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)

    # Concatenate the formatted strings to get the 24-hour time
    time_24_hour = hour_str + minute_str

    return time_24_hour

# Example outputs:
print(convert_to_24_hour_format(1, 00, "am"))  
print(convert_to_24_hour_format(11, 00, "pm"))  
