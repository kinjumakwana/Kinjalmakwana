mylist=[5,10,15,20,3,15,25,20,30,10,100]
uniques=[]
for num in mylist:
    if num not in uniques:
        uniques.append(num)
print(uniques)