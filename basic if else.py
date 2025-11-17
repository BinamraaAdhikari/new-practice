a=int(input("Enter a number:"))   
b=int(input("Enter a number:"))   
c=int(input("Enter a number:"))   
d=int(input("Enter a number:"))   
if a>b and a>c and a>d:
    print(a,"is the greatest number")
elif b>a and b>c and b>d:
    print(b,"is the greatest number")
    
elif c>b and c>a and c>d:
    print(c,"is the greatest number")
    
elif d>b and d>c and d>a:
    print(d,"is the greatest number")
elif a==b==c==d:
    print("They are all same number")
else:
    print("Invalid number")
    
    

                                  
