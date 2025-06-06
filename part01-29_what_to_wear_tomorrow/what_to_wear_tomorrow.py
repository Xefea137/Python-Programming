"""
Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

Some examples of expected behaviour:
What is the weather forecast for tomorrow?
Temperature: 21
Will it rain (yes/no): no
Wear jeans and a T-shirt

What is the weather forecast for tomorrow?
Temperature: 11
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well

What is the weather forecast for tomorrow?
Temperature: 7
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you

What is the weather forecast for tomorrow?
Temperature: 3
Will it rain (yes/no): yes
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you
Make it a warm coat, actually
I think gloves are in order
Don't forget your umbrella!
"""

temp = int(input("What is the weather forecast for tomorrow? "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")
if rain == "yes":
    print("Don't forget your umbrella!")
if temp < 21:
    print("I recommend a jumper as well")
if temp < 11:
    print("Take a jacket with you")
if temp < 6:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")