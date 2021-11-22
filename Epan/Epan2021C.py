count = 0
count20 = 0
sum = 0
while sum < 1200:
    count = count + 1
    print "Type the tip of the ", count, "th day: "
    tip = input()
    if tip > 20:
        count20 = count20 + 1
    sum = sum + tip
print "It takes ", count, " days to collect 1200 euros"
rate = float(count20) / count * 100
print "The percentage of days when the tip was greater than 20 euros is ", rate, "%"
change = sum - 1200
if change > 0:
    print "Surplus: ", change, "euros"
    if change > 50:
        print "The surplus is enough to buy a helmet of 50 euros"