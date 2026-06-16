Letters={1,1,2,3,4}
print(Letters)
print(type(Letters))
name={"first_name":"Kirabo","last_name":"Eria"}
print(name)
print(type(name))
del name["first_name"]
print(name)
Letters.add(5)
print(Letters)
Letters.remove(1)
print(Letters)
Letters.discard(2)
print(Letters)
Letters.update({6,7})
print(Letters)
nos=[1,2,3,4,5]
print(nos)
nos.append(6)
print(nos)
nos.insert(0,0)
print(nos)
nos.remove(3)
print(nos)
nos.pop()
print(nos)
nos.pop(1)
print(nos)
lett=list(Letters)
print(lett)
boys=dict(name=dict(first_name="Kirabo"),age=20,course="Computer Science")
print(boys)
a=[[8,6],[2,3,4,5]]
for i in a:
    for j in i:
        print(j,end=" ")
    print() 
cp=(1,2,3,4,5)
print(cp)
print(type(cp))   
cps=list(cp)
print(cps)
a.insert(1,9)
print(a)
a.extend([10,11])
print(a)
a.append([12,13])
print(a)
b=[1,2,3,4,5]
b.remove(3)
print(b)
b.pop(0)
print(b)
cpw=cp*3
print(cpw)





















