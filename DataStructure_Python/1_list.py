#List Manipulation Methods In python

mylist1=['Tony','Michael','Denise','Mark']
mylist2=['Boi','LOl','xd']

#accesing through indexing 
print(mylist1[0]+" is at zero index" )
print(mylist1[2]+" is at 2nd Index")

#length of list 
print(str(len(mylist1))+" is length of list")

#list slicing
print(mylist1[1:3])
print(mylist1[0:])
print(mylist1[:-1])

#append and insert to list 
mylist1.append("Bill")
mylist1.append("Elon")
mylist1.insert(4,"GG")

print(mylist1)

#extending to list
mylist1.extend(mylist2)

print(mylist1)

#delete and remove and pop
del mylist1[1]
mylist1.remove('Boi')
mylist1.pop(4)
print(mylist1)

#reverse the List
mylist1.reverse()
print(mylist1)

#if in,for in

if "GG" in mylist1:
    print("GG in mylist1")
else:
    print("not in mylist1")
for i in mylist1:
    print(i)



