a=int(input("Enter the marks you obtained:"))
if a>100:
    print("Badmoshi nahi mitr")
elif a<=100 and a>=90:
    print("COngrats you got an A+")
elif a<90 and a>=80:
    print("Congrats you got an A")
elif a<80 and a>=60:
    print("You got B+")
elif a<60 and a>=40:
    print("You got a C")
elif a<=0:
    print("GET OUT")
else:
    print("You failed buddy")
