x = [1,3,1,4,-7,12,22,-31,1,6,8,9,4]


maxScore = 0
currentMax = 0
seq = []
for i in range(len(x)-1):
    if x[i] <= x[i+1]:
        currentMax += 1
    if currentMax >= maxScore:
        maxScore = currentMax+1
        seq = x[i-maxScore+2:i]
    if x[i] > x[i+1]:
        currentMax = 0
print (seq)
print (maxScore)

