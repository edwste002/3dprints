import math

import io

def print_to_string(*args, **kwargs):
    output = io.StringIO()
    print(*args, file=output, **kwargs)
    contents = output.getvalue()
    output.close()
    return contents

radiusOnTop = 20
radiusOnBottom = 40

numberOfTreads = 8
lengthOfGear = 40

numberOfPointsOnRecessedArc = 8
numberOfPointsOnTread = 3

heightOfTread = 0.5
widthOfTread = 2

numberOfZDefinitionPoints = 10

topRadiusArcDistancePerTread = widthOfTread

topRadiusArcDistancePerRecess = ((2 * radiusOnTop * math.pi) - (numberOfTreads * widthOfTread)) / (numberOfTreads)

#calculate recess based on tread length
topRadiusArcDistancePerTreadAndRecess = (2 * radiusOnTop * math.pi) / numberOfTreads
arcPercentageForTopRadiusTreadAndRecess = (2 * math.pi) / numberOfTreads
arcPercentageForTopRadiusTread = widthOfTread / topRadiusArcDistancePerTreadAndRecess
arcPercentageForTopRecessOfTread = arcPercentageForTopRadiusTreadAndRecess - arcPercentageForTopRadiusTread


radiusSlopePerNumberOfZDefintionPoints = (radiusOnBottom - radiusOnTop) / numberOfZDefinitionPoints

#print('topRadiusArcDistancePerTreadAndRecess,topRadiusArcDistancePerTread,topRadiusArcDistancePerRecess')
#print(topRadiusArcDistancePerTreadAndRecess,topRadiusArcDistancePerTread,topRadiusArcDistancePerRecess)

#print('arcPercentageForTopRadiusTreadAndRecess,arcPercentageForTopRadiusTread,arcPercentageForTopRecessOfTread')
#print(arcPercentageForTopRadiusTreadAndRecess,arcPercentageForTopRadiusTread,arcPercentageForTopRecessOfTread)


cvt = []

def getArcRatio(arcLengthForPreviousRadius, newArcRadius):
    getCurrentRatio = arcLengthForPreviousRadius / ( 2 * newArcRadius * math.pi)
    return getCurrentRatio

def makePointsAlongArc(currentRadius,numberOfPoints,thetaStart,thetaEnd,currentZ):
    l=[]
    #fix wrap around issue
    thetaStep = abs(thetaEnd - thetaStart) / (numberOfPoints)
    #print('thetaStart,thetaStep,thetaEnd')
    #print(thetaStart,thetaStep,thetaEnd)
    for i in range(numberOfPoints):
        #print(i,'i cos sin', math.cos(thetaStart + thetaStep*i), math.sin(thetaStart + thetaStep*i))
        #print('cos sin')
        #print(math.cos(thetaStart + thetaStep*i))
        #print(math.sin(thetaStart + thetaStep*i))
        ll=[currentRadius * math.cos(thetaStart + thetaStep*i),
              currentRadius * math.sin(thetaStart + thetaStep*i),
              currentZ]
        l.append(ll)
    ll=[currentRadius * math.cos(thetaStart + thetaStep*numberOfPoints),
              currentRadius * math.sin(thetaStart + thetaStep*numberOfPoints),
              currentZ]
    l.append(ll)
    #print('----')
    #print(l)
    return l


cvt = []
for z in range(numberOfZDefinitionPoints+1):
    #print('----z-----')
    currentRadius = treadRecessHeight = radiusOnTop + z*radiusSlopePerNumberOfZDefintionPoints
    treadHeight = treadRecessHeight + heightOfTread
    getCurrentCircumferenceTreadAndRecessPercentage = getArcRatio(topRadiusArcDistancePerTreadAndRecess, currentRadius)
    getCurrentCircumferenceTreadPercentage = getArcRatio(topRadiusArcDistancePerTread, currentRadius)
    getCurrentCircumferenceTreadRecessPercentage = getArcRatio(topRadiusArcDistancePerRecess, currentRadius)

    #print(getCurrentCircumferenceTreadAndRecessPercentage,getCurrentCircumferenceTreadPercentage,getCurrentCircumferenceTreadRecessPercentage)
    #print('getCurrentCircumferenceTreadAndRecessPercentage,getCurrentCircumferenceTreadPercentage,getCurrentCircumferenceTreadRecessPercentage')
    for t in range(numberOfTreads):
        #print('-----------------'+str(t)+'----------------------------'+str(getCurrentCircumferencePercentageOnTread)+' ' + str(treadHeight))
        cvt = cvt + makePointsAlongArc(treadHeight,numberOfPointsOnTread,(2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*t,(2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*t + (2*math.pi) * getCurrentCircumferenceTreadPercentage,currentRadius)
        cvt = cvt + makePointsAlongArc(currentRadius,numberOfPointsOnRecessedArc,(2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*t + (2*math.pi) * getCurrentCircumferenceTreadPercentage,(2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*(t+1),currentRadius)
    #add other side to this
    if not z==0:
        cvt = cvt + makePointsAlongArc(currentRadius,numberOfPointsOnTread + numberOfPointsOnRecessedArc, (2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*(numberOfTreads+1),0,currentRadius)


with open('output.txt','w') as f:
    s = print_to_string(cvt)
    f.write(s)
