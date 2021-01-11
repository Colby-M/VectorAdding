import math
convert = math.pi / 180
convert2 = 180 / math.pi
Vector = []
Xs1 = []
Ys1 = []
Xs=[]
Ys=[]
Degree=[]
xsum=0
ysum=0
total=0
Deg=0
totalDeg=0
print('input a -1 to go to next array')
while 1:
    Inp = float(input('vector = '))
    if Inp == (-1):
        break
    Vector.append(Inp)
while 1:
    Inp2 = float(input('Degree (0-360) = '))
    if Inp2==(-1):
        break
    Degree.append(Inp2)
if len(Vector)==len(Degree):

 for num in Degree:
    Xs1.append(math.cos(num*convert))
    Ys1.append(math.sin(num*convert))
 for num in range(len(Vector)):
  G=Vector[num]
  H=Xs1[num]
  D=G*H
  A=Ys1[num]
  Y=G*A
  Xs.append(D)
  Ys.append(Y)
 for num in range(len(Vector)):
    xsum = xsum + Xs[num]
    ysum = ysum + Ys[num]
 total = math.sqrt(xsum*xsum+ysum*ysum)
 print(total)
 Deg = math.atan(ysum/xsum)
 totalDeg = Deg * convert2
 if xsum<0 and ysum<0:
    totalDeg = totalDeg + 180
 elif xsum<0:
    totalDeg = totalDeg + 90
 elif ysum<0:
    totalDeg = totalDeg + 360
 print(totalDeg)
else:
    print('input same number of magnitudes and degrees!')
