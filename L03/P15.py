pm25 = float(input("PM2.5: "))

if pm25 <= 12.0:
    category = "Good"
elif pm25 <= 35.4:
    category = "Moderate"
elif pm25 <= 55.4:
    category = "Unhealthy for Sensitive Groups"
elif pm25 <= 150.4:
    category = "Unhealthy"
elif pm25 <= 250.4:
    category = "Very Unhealthy"
else:
    category = "Hazardous"

print("AQI:", category)
