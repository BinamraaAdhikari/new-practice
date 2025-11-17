d={}
a=input("Enter your name:")
b=input("Enter your favorite language:")
d.update({a:b})
c=input("Enter your name:")
e=input("Enter your favorite language:")
d.update({c:e})
f=input("Enter your name:")
g=input("Enter your favorite language:")
d.update({f:g})
i=input("Enter a persons name:").lower()
if i in d:
    print("The favorite language of",i,"is:",d[i])     
else:
    print("Name not found")                                          
                                        
