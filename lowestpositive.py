arr = [ -1, 1, -2 , 3]

def getLowestPositive(arr):
    sorted_arr = [ i for i in sorted(arr) if i > 0 ]
    previous = 0
    if len(sorted_arr) == 0 :
        result =  1
    else:
        for i in sorted_arr:
            if previous == 0 :
                if i > 1 :
                    return 1
                else:
                    previous = i+1
            else:
                if i > previous :
                    return previous
                else:
                    previous = i+1
    return None

result= getLowestPositive(arr)
if result is None:
    print(sorted_arr[-1]+1)
else:
    print(result)