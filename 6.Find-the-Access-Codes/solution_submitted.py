def solution(l):
    l.reverse()

    parent= []
    child = []
    count = 0
    
    l1 = l
    for i in range(len(l1)):
        #print(i)
        l2 = l1[i+1:]
        for j in range(len(l2)):
            if l1[i] % l2[j] == 0:
                parent.append(i)
                child.append(j+i+1)

    child.sort()

    if child[0] in parent:

        parentList = parent[parent.index(child[0]):]

        groupList = {}
        for i in child:
            groupList[str(i)] = 0

        for i in child:    
            groupList[str(i)] += 1
            
        for i in parentList:
            if str(i) in groupList:
                count += groupList[str(i)]
        
        return count
    else:
        return count