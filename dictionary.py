#merging a and b
a={1:10,2:20,3:30}
b={4:33,5:23}
c=a
c.update(b)
print(a)

#sum the value
a={1:10,2:20,3:30}
sum=0
for i in a.values():
    sum=sum+i
    
print(sum)    

#frequency
a=[1,2,1,2,3,3,2,3,3,4,4,4,1,2]
dict={}
for i in a:
    if i in dict.keys():
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)        
