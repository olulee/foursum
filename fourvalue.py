fval= [5,10,15,20,25,30]
sval= [5,20,25,30,35,40]
ival= [2,10,15,20,25,30]
tval= [5,10,20,25,30,20]

print("fval list:" + str(fval))

print("sval list:" + str(sval))

print("ival list:" + str(ival))

print("tval list:" + str(tval))

result=[]

for x in range(0, len(fval)):
	result.append(fval[x]+sval[x]+ival[x]+tval[x])
print("my result:" + str(result))
