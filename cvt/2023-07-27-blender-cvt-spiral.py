import math

radiusOnTop = 20
radiusOnBottom = 40

numberOfTreads = 8
lengthOfGear = 40

numberOfPointsOnRecessedArc = 8
numberOfPointsOnTread = 3

heightOfTread = 0.5
widthOfTread = 2

arcDistancePerTreadAndRecess = (2 * radiusOnTop * math.pi) / numberOfTreads
arcPercentageForTopOfTread = widthOfTread / arcDistancePerTreadAndRecess
arcPercentageForRecessOfTread = 1 - (widthOfTread / arcDistancePerTreadAndRecess )

#print(arcDistancePerTreadAndRecess)
#print(arcPercentageForTopOfTread)

#numberOfXYDefinitionPoints = 20
numberOfZDefinitionPoints = 10

#numberOfZDefinitionPoints = 1

#def positionOfXYOfTreadAtZ(z=0,treadNumber=0,isTread=False):
#    return 

#figure out mesh position...see if you can do it in layers...if so do that    

cvt = []

radiusSlopePerNumberOfZDefintionPoints = (radiusOnBottom - radiusOnTop)

def getArcRatio(arcDistancePerTreadAndRecess, currentRadius):
    getCurrentCircumferencePercentage = arcDistancePerTreadAndRecess / (2 * currentRadius * math.pi)
    #print('arc length')
    #print(getCurrentCircumferencePercentage)
    return getCurrentCircumferencePercentage

def makePointsAlongArc(currentRadius,numberOfPoints,thetaStart,thetaEnd):
    l=[]
    thetaStep = (thetaEnd - thetaStart) / numberOfPoints
    #print(thetaStart,thetaStep,thetaEnd)
    for i in range(numberOfPoints):
        ll=[currentRadius * math.cos(thetaStart + thetaStep*i),
              currentRadius * math.sin(thetaStart + thetaStep*i),
              (z/numberOfZDefinitionPoints)*lengthOfGear]
        l.append(ll)
    #print('----')
    #print(l)
    return l


cvt = []
for z in range(numberOfZDefinitionPoints):
    currentRadius = treadRecessHeight = radiusOnTop + (z/numberOfZDefinitionPoints)*radiusSlopePerNumberOfZDefintionPoints
    treadHeight = treadRecessHeight + heightOfTread
    getCurrentCircumferencePercentage = getArcRatio(arcDistancePerTreadAndRecess, currentRadius)
    for t in range(numberOfTreads):
        cvt = cvt + makePointsAlongArc(currentRadius,
                                       numberOfPointsOnRecessedArc,
                                       (2*math.pi)*getCurrentCircumferencePercentage*t,
                                       (2*math.pi)*getCurrentCircumferencePercentage*t + (2*math.pi)*getCurrentCircumferencePercentage*arcPercentageForRecessOfTread)
                                        
        cvt = cvt + makePointsAlongArc(treadHeight,
                                       numberOfPointsOnTread,
                                       (2*math.pi)*getCurrentCircumferencePercentage*t + (2*math.pi)*getCurrentCircumferencePercentage*arcPercentageForRecessOfTread,
                                        (2*math.pi)*getCurrentCircumferencePercentage*(t+1))


print(cvt)
