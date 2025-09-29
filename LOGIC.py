n=input("enter: ")
print(n)
k=n.split()
print(k)
list2=[]
if len(k)==1:
    j=k[0][0:3]
    print(j)
else:
    for i in k:
        print(i)
        print(i[0])
        
        list2.append(i[0].upper())
        seperator=""
        u=seperator.join(list2)
        print(u)
