occ = 0
count = 0
sum = 0
for i in range(100):
    dep = int(input("Type the number of departures: "))
    while dep < 0 or dep > occ:
        print "We have ", occ, " occupied rooms"
        dep = int(input("Type the number of departures: "))
    occ = occ - dep
    arr = int(input("Type the number of arrivals: ")
    while arr < 0 or arr > 50-occ:
        print "We have ", 50-occ, " rooms available"
        arr = int(input("Type the number of arrivals: ")
    occ = occ + arr
    if occ == 50:
        count = count + 1
    sum = sum + occ
print "full house for ", count, "days"
avg = sum / 100.0
print "average occupancy ", avg
total = 80 * sum
print "total revenue in 100 days", total, "euros"