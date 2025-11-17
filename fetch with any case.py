words={
    "dog":"Kukur",
       "cat":"Biralo",
       "cow":"Gai",
       "tiger":"Bagh"
       }
a=input("Enter the name of the animal:").lower()
if a in words:
    print(a,"is known as",words[a],"in Nepali language")
else:
    print("Animal not found")
                                                
                                     
