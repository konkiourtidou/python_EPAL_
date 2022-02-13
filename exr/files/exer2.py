#Anoigma tou arxeiou num.txt kai eggrafh twn artiwn ari8mwn pou plhktrologeite, enan se ka8e grammi
f=open("num.txt","w")
a=raw_input("Dose ari8mo - 0 gia termatismo")
while a!="0":
	f.write(a)
	f.write("\n")
	a=raw_input("Dose ari8mo - 0 gia termatismo")

#kleisimo tou arxeiou
f.close()

#Anoigma tou arxeiou num.txt gia anagnwsh
f=open("num.txt")

#diasxish tou arxeiou kai euresh tou Mesou Orou twn arithmwn pou periexei ka8ws kai tou megistou
sum=0
count=0.0
max=int(f.readline())
for line in f:
	sum=sum+int(line)
	count=count+1
	if int(line)>max:
		max=int(line)
if count!=0:
	mo=sum/count
	#Emfanish twn apotelesmatwn
	print "Megistos o: ",max," Mesos Oros: ",mo
else:
	print "To arxeio den periexei ariumous"

f.close()
