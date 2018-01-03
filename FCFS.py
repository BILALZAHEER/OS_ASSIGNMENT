file=open("FCFS.txt","r")
p=[]
dur=[]
cp=[]
ord=[]
arr=[]
tot=0
ttime=[]
ind=0
for val in file :
    value=[int(x) for x in val.split()]
    p.append((value[0]))
    dur.append(value[1])
    ord.append(value[2])
    arr.append(value[3])
    cp.append(value[3])
arr.sort()
for x in arr:
    for y in range(len(cp)):
        if (x==cp[y]):
            ind=y
    tot+=dur[ind]
    ttime.append(tot)
    print 'p'+str(p[ind]),
print
for x in ttime:
    print x,
print
print "Time : "+str(tot)
file.close()