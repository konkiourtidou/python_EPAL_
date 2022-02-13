count=0
sum=0
f=open("bathmoi.txt")
for line in f:
	x=line
	for i in range(len(line)):
		if line[i]==",":
			sum=sum+int(x[i+1:])
			count=count+1
mo=sum/count
print mo
