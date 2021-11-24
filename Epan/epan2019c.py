occ = 0
count = 0
sum = 0
#Για καθένα από τα 100 δωμάτια
for i in range(100):
    #Είσοδος αναχωρήσεων με έλεγχο εγκυρότητας
    dep = int(input("Type the number of departures: "))
    while dep < 0 or dep > occ:
        print "We have ", occ, " occupied rooms"
        dep = int(input("Type the number of departures: "))
    occ = occ - dep
    #Είσοδος αφίξεων με έλεγχο εγκυρότητας
    arr = int(input("Type the number of arrivals: ")
    while arr < 0 or arr > 50-occ:
        print "We have ", 50-occ, " rooms available"
        arr = int(input("Type the number of arrivals: ")
    occ = occ + arr
    if occ == 50:
        count = count + 1
    sum = sum + occ
#Έξοδος αποτελεσμάτων
print "full house for ", count, "days"
avg = sum / 100.0
print "average occupancy ", avg
total = 80 * sum
print "total revenue in 100 days", total, "euros"
