def solution(xs):
    xs.sort(reverse=True)
    
    negativeValues = []
    positiveValues = []

    if len(xs) > 1:
        for i in xs:
            if i > 0:
                positiveValues.append(i)
            if i < 0:
                negativeValues.append(i)
        if len(negativeValues) % 2 == 1:
            negativeValues.pop(0) 
        if len(positiveValues) > 0 or len(negativeValues) > 0:
            panelsToKeep = positiveValues + negativeValues
            maxValue = 1
            for i in panelsToKeep:
                maxValue *= i
            return str(maxValue)
        else:
            return '0'
    else:
        return str(xs[0])