list=["apple","ball","cat","dog",2,3,4,5]


j=[2,4,5,7]
new_list=[list[i] for i in j]

for l, a in enumerate(new_list, start=1):
    print(f"{l}) {a} ")
 
