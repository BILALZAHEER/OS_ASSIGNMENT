file=open("SJF.txt","r")
dur=[]
cp=[]
p=[]
arr=[]
ord=[]
tot=0
tval=[]
for l in file:
     vals = [int(x) for x in l.split()]
     dur.append(vals[1])
     cp.append(vals[1])
     p.append(vals[0])
     ord.append(vals[2])
     arr.append(vals[3])
dur.sort()
for val in dur:
    tot += int(val)
    tval.append(tot)
    for val2 in range(len(cp)):
        if (val==cp[val2]):
            print 'p'+str(p[val2]),
print
for val in tval:
    print val,
print
print "Time : ",
print tot
file.close()