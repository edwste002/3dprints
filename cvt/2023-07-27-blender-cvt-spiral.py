import math

radiusOnTop = 20
radiusOnBottom = 40

numberOfTreads = 8
lengthOfGear = 40

heightOfTread = 2
widthOfTread = 2

arcDistancePerTreadAndRecess = (radiusOnTop**2 * math.pi) / numberOfTreads
arcPercentageForTopOfTread = widthOfTread / arcDistancePerTreadAndRecess 



#numberOfXYDefinitionPoints = 20
#numberOfZDefinitionPoints = 40

numberOfZDefinitionPoints = 1

#def positionOfXYOfTreadAtZ(z=0,treadNumber=0,isTread=False):
#    return 

#figure out mesh position...see if you can do it in layers...if so do that    

cvt = []


radiusSlopePerNumberOfZDefintionPoints = (radiusOnBottom - radiusOnTop) / lengthOfGear

for z in range(numberOfZDefinitionPoints):
    currentRadius = treadRecessHeight = radiusOnTop + z*radiusSlopePerNumberOfZDefintionPoints
    treadHeight = treadRecessHeight + heightOfTread
    for t in range(numberOfTreads):
        p1 = [treadRecessHeight * math.cos((math.pi/numberOfTreads) * t),
              treadRecessHeight * math.sin((math.pi/numberOfTreads) * t)]
        p2 = [treadHeight * math.cos((math.pi/numberOfTreads) * t),
              treadHeight * math.sin((math.pi/numberOfTreads) * t)]
        p3 = [treadHeight * math.cos((math.pi/numberOfTreads) * (t + arcPercentageForTopOfTread)),
              treadHeight * math.sin((math.pi/numberOfTreads) * (t + arcPercentageForTopOfTread))]
        p4 = [treadRecessHeight * math.cos((math.pi/numberOfTreads) * (t + arcPercentageForTopOfTread)),
                                           treadRecessHeight * math.sin((math.pi/numberOfTreads) * (t + arcPercentageForTopOfTread))]

        cvt.append(p1)
        cvt.append(p2)
        cvt.append(p3)
        cvt.append(p4)

print(cvt)
