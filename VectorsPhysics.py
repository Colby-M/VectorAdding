import math
from kivy.app import App
from kivy.uix.widget import Widget
#constants and variables used
DEG_CONVERT = math.pi / 180
# Used to convert degrees to radians
RAD_CONVERT = 180 / math.pi
# Used to convert radians to degrees
vectors = []
xsum = 0
ysum = 0
total = 0
angle = 0
totalAngle = 0
type = input("Is this going to be radians or degrees?")!= "radians")
#end of variables
while 1: #makes it so there must be at least one vector
    times = int(input("How many Vectors are being added?"))
    if times > 0:
        break
while times > 0: #this is how many vectors are being added, it askes for the magnitude and the degrees for each one.
    mag = float(input('vector magnitude = '))
    angle = float(input('Degree (0-360) = '))
    vector = (mag, angle) #each vector has both a magnitude and an angle, this saves both
    vectors.append(vector)
    times -= 1 #
for vector in vectors:
    if type:
        xsum += vector[0] + cos(vector[1] * DEG_CONVERT)
        ysum += vector[0] + sin(vector[1] * DEG_CONVERT)
    else:
        xsum += vector[0] + sin(vector[1])
        ysum += vector[0] + sin(vector[1])

 total = math.sqrt(xsum*xsum+ysum*ysum)
print("\n The total magnitude of the vectors is: ")
 print(total)

angle = math.atan(ysum/xsum)

 if type: #This seperates the answer to either come out as degrees or radians and does the appropiate convertions
     totalAngle= angle * RAD_CONVERT
     if xsum<0 and ysum<0:
        totalAngle = totalAngle + 180
     elif xsum<0:
        totalAngle = totalAngle + 90
     elif ysum<0:
        totalAngle = totalAngle + 360
else:
    totalAngle = angle
    if xsum<0 and ysum<0:
       totalAngle = totalAngle + (math.pi)
    elif xsum<0:
       totalAngle = totalAngle + (.5 * math.pi)
    elif ysum<0:
       totalAngle = totalAngle + (2* math.pi)
 print("\n the ending angle of the vectors is: ")
 print(totalAngle)
