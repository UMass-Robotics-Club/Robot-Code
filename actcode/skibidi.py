totalset = []

for skib in ['a','b','c']:
    for b in ['a','b','c']:
        for a in ['a','b','c']:
            for c in ['a','b','c']:
                mysr = skib + a + b + c
                totalset.append(mysr)
                
#print(totalset)

setX = []
for i in range(0, len(totalset)):
    if totalset[i].count('b') >= 2:
        setX.append(totalset[i])

setY = []
for i in range(0, len(totalset)):
    if not 'cc' in totalset[i]:   
        setY.append(totalset[i])
setZ = []
for i in range(0, len(totalset)):
    if totalset[i].count('c') >= 1:
        if 'ca' in totalset[i] and totalset[i].count('c') == 1:
            setZ.append(totalset[i])
        elif 'caca' in totalset[i]:
            setZ.append(totalset[i])
        
    else:
        setZ.append(totalset[i])    

setX = set(setX) 
setY = set(setY)
setZ = set(setZ)
yz = setY.union(setZ)
xy = setX.union(setY)
xz = setX.union(setZ)
print(setX)

print(setX.issubset(setY))
print(setY.issubset(setX))
print(setX.issubset(setZ))
print(setZ.issubset(setX))
print(setY.issubset(setZ))
print(setZ.issubset(setY))

# print(xy.issubset(xz))
# print(xz.issubset(xy))
# print(yz.issubset(xz))
# print(xz.issubset(yz))
# print(xy.issubset(yz))
# print(yz.issubset(xy))
  
