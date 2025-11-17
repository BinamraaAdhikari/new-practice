a=int(input("Enter the marks obtained in Science:"))
b=int(input("Enter the marks obtained in Math:"))
c=int(input("Enter the marks obtained in Health:"))
total=(100)*(a+b+c)/300

if total>=40 and a>33 and b>33 and c>33:
    print("You passed with",total,"%")
else:
    print("You failed with",total,"%")
                                                                                    
                                          
