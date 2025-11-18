l=[]
for a in range (6):
    b=input("Enter your name:")
    l.append(b)
    if b.lower().startswith("s"):
        print("Hello",b)
    else:
        print("No entry for you",b)
