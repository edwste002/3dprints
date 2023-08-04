import math

import io

def print_to_string(*args, **kwargs):
    output = io.StringIO()
    print(*args, file=output, **kwargs)
    contents = output.getvalue()
    output.close()
    return contents

radiusOnTop = 40
radiusOnBottom = 80

numberOfTreads = 8

numberOfPointsOnRecessedArc = 8
numberOfPointsOnTread = 3

heightOfTread = 3
widthOfTread = 2

numberOfZDefinitionPoints = 15

topRadiusArcDistancePerTread = widthOfTread
topRadiusArcDistancePerRecess = ((2 * radiusOnTop * math.pi) - (numberOfTreads * widthOfTread)) / (numberOfTreads)

#calculate recess based on tread length
topRadiusArcDistancePerTreadAndRecess = (2 * radiusOnTop * math.pi) / numberOfTreads
arcPercentageForTopRadiusTreadAndRecess = (2 * math.pi) / numberOfTreads
arcPercentageForTopRadiusTread = widthOfTread / topRadiusArcDistancePerTreadAndRecess
arcPercentageForTopRecessOfTread = arcPercentageForTopRadiusTreadAndRecess - arcPercentageForTopRadiusTread

radiusSlopePerNumberOfZDefintionPoints = (radiusOnBottom - radiusOnTop) / numberOfZDefinitionPoints

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

cvtLayers = []
cvtSections = []

for z in range(numberOfZDefinitionPoints+1):
    #print('----z-----')
    currentRadius = treadRecessHeight = radiusOnTop + z*radiusSlopePerNumberOfZDefintionPoints
    treadHeight = treadRecessHeight + heightOfTread
    getCurrentCircumferenceTreadAndRecessPercentage = getArcRatio(topRadiusArcDistancePerTreadAndRecess, currentRadius)
    getCurrentCircumferenceTreadPercentage = getArcRatio(topRadiusArcDistancePerTread, currentRadius)
    getCurrentCircumferenceTreadRecessPercentage = getArcRatio(topRadiusArcDistancePerRecess, currentRadius)
    cvtSections = []
    #print(getCurrentCircumferenceTreadAndRecessPercentage,getCurrentCircumferenceTreadPercentage,getCurrentCircumferenceTreadRecessPercentage)
    #print('getCurrentCircumferenceTreadAndRecessPercentage,getCurrentCircumferenceTreadPercentage,getCurrentCircumferenceTreadRecessPercentage')
    for t in range(numberOfTreads):
        #print('-----------------'+str(t)+'----------------------------'+str(getCurrentCircumferencePercentageOnTread)+' ' + str(treadHeight))
        m = makePointsAlongArc(treadHeight,numberOfPointsOnTread,(2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*t,(2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*t + (2*math.pi) * getCurrentCircumferenceTreadPercentage,currentRadius)
        cvtSections.append(m)
        m = makePointsAlongArc(currentRadius,numberOfPointsOnRecessedArc,(2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*t + (2*math.pi) * getCurrentCircumferenceTreadPercentage,(2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*(t+1),currentRadius)
        cvtSections.append(m)
        
    #add other side to this
    if not z==0:
        m = makePointsAlongArc(currentRadius,numberOfPointsOnTread + numberOfPointsOnRecessedArc, (2*math.pi) * getCurrentCircumferenceTreadAndRecessPercentage*(numberOfTreads+1),0,currentRadius)
        cvtSections.append(m)
    else:
        #need special case on top layer
        #add same point
        lastpiece = []
        for i in range(numberOfPointsOnTread + numberOfPointsOnRecessedArc):
            lastpiece.append(m[-1])
        cvtSections.append(lastpiece)
    cvtLayers.append(cvtSections)

cvt = []
#print(cvtLayers)
#make square patterns with widget creation
for i,vnt in enumerate(cvtLayers):
    #each tread section
    if not i == len(cvtLayers) - 1:
        for j, vcs in enumerate(vnt):
            #for each tread section

        
            for k, vs in enumerate(vcs):
            #print(len(vcs))
                if not k == len(vcs) - 1:
                
            #print(i,j,k)
            #print(((cvtLayers[i])[j])[k])
                    cvt.append([((cvtLayers[i])[j])[k],((cvtLayers[i])[j])[k+1],
                            ((cvtLayers[i+1])[j])[k+1],((cvtLayers[i+1])[j])[k]])

            if not j == len(vnt) - 1:
                #print(i,j,k)
                cvt.append([((cvtLayers[i])[j])[-1],((cvtLayers[i])[j+1])[0],
                            ((cvtLayers[i+1])[j+1])[0],((cvtLayers[i+1])[j])[-1]])

                
            
with open('output.txt','w') as f:
    s = print_to_string(cvt)
    f.write(s)
