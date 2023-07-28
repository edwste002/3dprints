import math

radiusOnTop = 20
radiusOnBottom = 40

numberOfTreads = 8
lengthOfGear = 40

heightOfTread = 0.5
widthOfTread = 2

arcDistancePerTreadAndRecess = (2 * radiusOnTop * math.pi) / numberOfTreads
arcPercentageForTopOfTread = widthOfTread / arcDistancePerTreadAndRecess 

print(arcDistancePerTreadAndRecess)
print(arcPercentageForTopOfTread)

#numberOfXYDefinitionPoints = 20
numberOfZDefinitionPoints = 10

#numberOfZDefinitionPoints = 1

#def positionOfXYOfTreadAtZ(z=0,treadNumber=0,isTread=False):
#    return 

#figure out mesh position...see if you can do it in layers...if so do that    

cvt = []

radiusSlopePerNumberOfZDefintionPoints = (radiusOnBottom - radiusOnTop)

def getArcLength(arcDistancePerTreadAndRecess, currentRadius):
    getCurrentCircumferencePercentage = arcDistancePerTreadAndRecess / (2 * currentRadius * math.pi)
    return getCurrentCircumferencePercentage

def makePointsAlongArc(currentRadius,numberOfPoints,thetaStart,thetaEnd):
    l=[]
    thetaStep = (thetaEnd - thetaStart) / numberOfPoints
    for i in range(numberOfPoints):
        ll=[currentRadius * math.cos(thetaStart + thetaStep*i),
              currentRadius * math.sin(thetaStart + thetaStep*i),
              (z/numberOfZDefinitionPoints)*lengthOfGear]
        l.append(ll)

for z in range(numberOfZDefinitionPoints):
    currentRadius = treadRecessHeight = radiusOnTop + (z/numberOfZDefinitionPoints)*radiusSlopePerNumberOfZDefintionPoints
    treadHeight = treadRecessHeight + heightOfTread
    getCurrentCircumferencePercentage = getArcLength(arcDistancePerTreadAndRecess, currentRadius)
    for t in range(numberOfTreads): 
        p1 = [treadRecessHeight * math.cos(((2*math.pi)*getCurrentCircumferencePercentage*t)),
              treadRecessHeight * math.sin(((2*math.pi)*getCurrentCircumferencePercentage*t)),
              (z/numberOfZDefinitionPoints)*lengthOfGear]
        p2 = [treadHeight * math.cos(((2*math.pi)*getCurrentCircumferencePercentage*t)),
              treadHeight * math.sin(((2*math.pi)*getCurrentCircumferencePercentage*t)),
              (z/numberOfZDefinitionPoints)*lengthOfGear]
        p3 = [treadHeight * math.cos(((2*math.pi)*getCurrentCircumferencePercentage*(t+arcPercentageForTopOfTread))),
              treadHeight * math.sin(((2*math.pi)*getCurrentCircumferencePercentage*(t+arcPercentageForTopOfTread))),
              (z/numberOfZDefinitionPoints)*lengthOfGear]
        p4 = [treadRecessHeight * math.cos(((2*math.pi)*getCurrentCircumferencePercentage*(t+arcPercentageForTopOfTread))),
              treadRecessHeight * math.sin(((2*math.pi)*getCurrentCircumferencePercentage*(t+arcPercentageForTopOfTread))),
              (z/numberOfZDefinitionPoints)*lengthOfGear]

        cvt.append(p1)
        cvt.append(p2)
        cvt.append(p3)
        cvt.append(p4)

print(cvt)
