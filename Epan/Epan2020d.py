def bubbleSort(n, v):
    for i in range(len(n)):
        for j in range(len(v)-1, i-1, -1):
            if v[j] > v[j-1]:
                v[j], v[j-1] = v[j-1], v[j]
                n[j], n[j-1] = n[j-1], n[j]

NAME = []
VATH = []
for i in range (200):
    n = raw_input("Enter a name: ")
    NAME.append(n)
    sum = 0
    for j in range(4):
        print "Enter the score of judge ", j+1
        v = int(input())
        while v < 1 or v > 100:
            print "Enter the score of judge ", j+1
            v = int(input())
        sum = sum + v
    VATH.append(sum)
bubbleSort(NAME, VATH)
print "qualify for the next phase"
sum = 0
for i in range(50):
    print NAME[i], VATH[i]
    sum = sum + VATH[i]
avrg = sum / 50.0
print "average score of competitors who advance to the next stage", avrg
if VATH[200] > 300:
    count = 300
else:
    count = 0
    while VATH[count] > 300:
        count = count +1
print "percentage of competitors with a score greater than 300 points", count/2.0, "%"