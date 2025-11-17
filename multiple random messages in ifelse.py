import random
a=int(input("Enter your age:")) 
if a>=18:
    print("You may enter")
else:
    m=["Nice try kid",
       "No entry for children",
       "Go eat candies kid",
       "Only for adults buddy"]        
    print(random.choice(m))       
