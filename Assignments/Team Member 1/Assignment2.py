import random

temp  = 0
while temp <= 80:
    temp = round(random.random() * 100,2)
    humidity = round(random.random() * 100,2)
    pressure = round(random.random() * 100,2)
    print("Temperature: ",temp,' °C')
    print("Humidity: ",humidity,'%\n')
    print("Pressure: ",pressure,'Pa\n')

else:
    print(f"High Temperature  of {temp}°C is detected !!!")
