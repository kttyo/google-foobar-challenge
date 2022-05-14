def solution(map):
    height = len(map)
    width = len(map[0])

    origin = {'x':0,'y':0,'w':0}
    destination = {
        'x':width-1,
        'y':height-1
    }

    def withinMap(dest):
        if dest['x'] >= 0 and dest['x'] < width and dest['y'] >= 0 and dest['y'] < height:
            return True
        else:
            return False

    def notUsedBefore(dest):
        notUsed = True        
        for i in range(len(paths)):
            for j in range(len(paths[i])):
                if paths[i][j]['x'] == dest['x'] and paths[i][j]['y'] == dest['y'] and paths[i][j]['w'] == dest['w']:
                    notUsed = False
        return notUsed
                


    def getNewPath(path):
        newPath = []

        for currentPos in path:
            right = {
                'x' : currentPos['x'] + 1,
                'y' : currentPos['y'],
                'w' : currentPos['w']
                }
            
            if withinMap(right):
                right['w'] += map[right['y']][right['x']]
                if right['w'] <= 1 and notUsedBefore(right):
                    if newPath.count(right) == 0:
                        newPath.append(right)

            left = {
                'x' : currentPos['x'] - 1,
                'y' : currentPos['y'],
                'w' : currentPos['w']
            }


            if withinMap(left):   
                left['w'] += map[left['y']][left['x']]
                if left['w'] <= 1 and notUsedBefore(left):
                    if newPath.count(left) == 0:
                        newPath.append(left)

            up = {
                'x' : currentPos['x'],
                'y' : currentPos['y'] - 1,
                'w' : currentPos['w']                   
            }

            if withinMap(up):
                up['w'] += map[up['y']][up['x']]
                if up['w'] <= 1 and notUsedBefore(up):
                    if newPath.count(up) == 0:
                        newPath.append(up)

            down = {
                'x' : currentPos['x'],
                'y' : currentPos['y'] + 1,
                'w' : currentPos['w']
            }

            if withinMap(down):
                down['w'] += map[down['y']][down['x']]
                if down['w'] <= 1 and notUsedBefore(down):
                    if newPath.count(down) == 0:
                        newPath.append(down)

        
        return newPath

    paths = []
    paths.append([origin])

    newPathPresent = True
    destinationNotReached = True

    loopCount = 0
    while newPathPresent and destinationNotReached:
        loopCount += 1

        path = getNewPath(paths[-1])
        if len(path) <= 0:
            newPathPresent = False
        else:
            paths.append(path)
            for i in range(len(path)):
                if path[i]['x'] == destination['x'] and path[i]['y'] == destination['y']:
                    destinationNotReached = False
                    break
    
    return loopCount+1