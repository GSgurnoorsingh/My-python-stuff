# list=[1,2,3,4,5,6,7,8,9]
# sum=0

# for feh in list:
#     sum=sum+feh
    
# print(sum)
tup=[(1,2),(3,4),(5,6),(7,8)]
#Now there are two ways to print the output
for i in tup:
    print(i)
    
#AND
for (a,b) in tup:
    print(a)
    print(b) #This thing is called tuple unpacking 
    
d={1:'one',2:'two',3:'three'}
for items in d:
    print(items)
    
for items in d.items(): #Here you can call d.values() only also if you want to deal with values only
    print(items)
    
for key,value in d.items():
    print(value)
    print(key) 