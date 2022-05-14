def solution(src, dest):
    moveOption = [6,10,15,17,-6,-10,-15,-17]

    fromSrc = [[src]]
    destSrc = [[dest]]

    def checkSrcUsed(direction,stepDest):
        if direction == 'start':
            tracker = fromSrc
        elif direction == 'goal':
            tracker = destSrc

        for i in range(len(tracker)):
            used = False
            if stepDest in tracker[i]:
                used = True
                break
            else:
                used = False
        return used

    def getAvailableStepAhead(src):
        stepAhead = []
        for srcPos in src:
            for move in moveOption:
                stepDest = srcPos + move
                if stepDest >= 0 and stepDest <= 63 and abs(srcPos % 8 - stepDest % 8) <=3:
                    if not checkSrcUsed('start',stepDest):
                        if stepDest not in stepAhead:
                            stepAhead.append(stepDest)
        return stepAhead

    def getAvailableStepBack(src):
        stepBack = []
        for srcPos in src:
            for move in moveOption:
                stepDest = srcPos + move
                if stepDest >= 0 and stepDest <= 63 and abs(srcPos % 8 - stepDest % 8) <=3:
                    if not checkSrcUsed('goal',stepDest):
                        if stepDest not in stepBack:
                            stepBack.append(stepDest)
        return stepBack

    while len(fromSrc[-1]) > 0:
        stepAhead = getAvailableStepAhead(fromSrc[len(fromSrc)-1])
        fromSrc.append(stepAhead)
        stepBack = getAvailableStepBack(destSrc[len(destSrc)-1])
        destSrc.append(stepBack)

    minimumSteps = 0
    if src != dest:
        for roundAhead in range(len(fromSrc)-1):
            for y in fromSrc[roundAhead]:
                for roundBack in range(len(destSrc)-1):
                    for z in destSrc[roundBack]:
                        if y == z:
                            minimumSteps = roundAhead + roundBack
                            return minimumSteps
              
    else:
        return int(0)