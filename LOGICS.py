#logic for spliting words in category and generating short form
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
        
        list2.append(i[0].upper())
        seperator=""
        u=seperator.join(list2)
        print(u)

#logic for dictionary updation
dict1={}
num=int(input("how many categories do u want: "))
for i in range(1,num+1):
    new_name=input("enter category type: ")
    new_cat=input("enter category : ")
    dict1.update({new_name:new_cat})
print(dict1)
