for i in range(3):
    a=input("Enter your username:")
    if a=="admin123":
        for z in range(3):
            b=input("Enter your password:")
            if b=="hello":
                print("Welcome back",a)
                break
        else:
            print("wrong password. Try again after 30 min ")
        break
else:
    print("Try again after 30 min")
    
