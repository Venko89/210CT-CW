def binarySearch(L, range_points):
    first = 0
    last = len(L)-1
    found = False

    if range_points[0] > range_points[1]:
        temp = range_points[0]
        range_points[0] = range_points[1]
        range_points[1] = temp
    while first<=last and not found:
        midpoint = (first + last)//2
        if L[midpoint] in range(range_points[0], range_points[1]):
            print("Found it: " + str(L[midpoint])
            found = True
            
        else:
            if range_points[0] < L[midpoint] or range_points[1] < L[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

testlist = [2,3,5,7,9,13]

print(binarySearch(testlist, [14,11]))

