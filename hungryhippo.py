hiWha = int(input("Hi! input a number: "))
primeCount = 0
iarray = [1, hiWha]
for i in range(hiWha//2):
    #print(i)
    #print("please print" + str(i))
    if i == 0 or i == 1:
        continue 
    #bruh idk what im do8ng12
    
    if (hiWha % i) == 0:
            if i == hiWha:
                continue
            #print(str(hiWha) + " is divisivle by this number. aka " +str(i))
            primeCount += 1
            iarray.append(i)
if primeCount > 0:
    print("Composite")
    print("These are its factors:")
    for item in iarray:
        print(item)
else: 
    print("Prime")