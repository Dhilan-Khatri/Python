Tuples=(1, 2, 3, 3, 2, 11)
lastTuples=len(Tuples)-1
startpos=0
flipflopped=True
while startpos< lastTuples:
    if (Tuples[startpos]!=Tuples[lastTuples]):
        flipflopped=False
    startpos+=1 
    lastTuples-=1    
if flipflopped:
    print("Tuples are same")
else:
    print("Tuples aren't flip-flopped")  

#Tuples2=Tuples[::-1]
#for i in range(5,-1,-1):
#    Tuples[i]

#if Tuples==lastTuples:
#    print("Tuples are same")
#else:
#    print("Tuples aren't flip-flopped")