def loadFile():
inFile = open('julyTemps.txt')
high = []
low = []
for line in inFile:
    fields = line.split()
    if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
        continue
    else:
        high.append(int(fields[1]))
        low.append(int(fields[2]))
return (low, high)
              
