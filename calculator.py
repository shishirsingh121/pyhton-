def add(x , y):
    return x + y
def sub(x , y):
    return x - y
def mult(x , y):
    return x * y
def div(x , y):
    return x / y
# while true():
print('choose the operator')
print("1.sum")
print("2.sub")
print("3.mult")
print("4.div")
while True:
    choose=input('choose(1/2/3/4)')
    if choose in ('1','2','3','4'):
        try :
            num1=int(input("enter the value of num1:"))
            num2=int(input('enter the value of num3:'))
        except errorvalue:
            print("error occur")
            continue
    if choose=='1':
        print('the sum of two is:',add(num1,num2))
    if choose=='2':
        print('the sub of two is:',sub(num1,num2))
    if choose=='3':
        print('the mult of two is:',mult(num1,num2))
    if choose=='4':
        print('the div of two is:',div(num1,num2)) 
    next_calulation=input("do you want to do again yes/no: ")
    if next_calulation=="no":
        break
    else:
        print("invalid number")
        
    
    
    
