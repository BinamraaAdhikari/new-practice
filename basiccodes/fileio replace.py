word="twinkle"
with open("table.txt") as f:
    data=f.read()
    newdata=data.replace(word,"winkle")
    
with open("table.txt","w") as f:
    f.write(newdata)
print(newdata)
