a=[1,2,6,7,88,9,80]
max=0
max2=0
index2=0
index=0
for i in range(len(a)):
    if a[i]> max:
        max2=max
        max=a[i]
        
        index=i
    elif a[i]>max2:
        max2=a[i]
        index2=i
        
print(max )   
print(max2)

#list is shorted
a=[1,2,3,4,55,66]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
    else:
        print("our list is not sorted")
        break
else:
    print("your lsit is shorted")

#pallindrome
a=[1,2,3,3,2,1]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
if a==b:
    print("pallindrome")