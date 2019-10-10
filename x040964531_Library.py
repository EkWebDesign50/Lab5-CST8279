#Lab 3
#Task 1 
#8
def FtoC(temp):
    """ This function takes the temperature in Farenheit and converts it into celsius. """
    temp = temp-32
    temp = temp*5/9
    return temp

#10
def mpg(miles,gallons):
    """ This function calculates takes distance traveled in miles and the amount of fuel used in 
    gallons and returns the milelage in miles per gallon. """
    return(miles/gallons)

#12
from math import pi, sqrt
def areaofcircle(r):
    """ This function takes a value for the radius of a circle and returns the area. """ 
    return(pi*r*r)

#Task 2
def DistanceBetweenPoints(x,y,x1,y1):
    """ This function calculates the distance between two points 
    with coordinates and returns the distance between the two points. """
    dx = x-x1 
    dy = y-y1
    dist = sqrt(dx**2 + dy**2) 
    return(dist)

#Lab 5 
#Task 1 
#1 
import gfxhat
from gfxhat import lcd, backlight
from random import randint
import time
def VeritcalLine(x):
    """ This function will display a vertical line at a given x coordiante on the gfx hat. """
    for y in range(63):
        lcd.set_pixel(x, y, 1)
    lcd.show()
#2
def HorizonatalLine(y):
    """ This functions will display a horizontal line at a given y coordiante """
    for x in range(127):
        lcd.set_pixel(x,y,1)
    lcd.show()
#3
def Staircase(x,y,w,h):
    """ This function will create a staircase at a specific Coordinate """
    while x<128 and y<64:
        for x in range(x, min(x+h, 127)):
            lcd.set(x,y,1)
        for y in range(y, min(y+w, 63)):
            lcd.set(x,y,1)
    lcd.show()
    
#4
def RandomPixel(s):
    """ This function will display a pixel on the gfx hat lcd screen for a given amount of time in seconds """
    x= randint(0,127)
    y= randint(0,63)
    lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(s)
    lcd.set_pixel(x,y,0)
    lcd.show()
 
#5
def clearBacklight(r,g,b): 
    """ This function will reset the backlight color. """
    backlight.set_all(r,g,b)
    backlight.show()



    

