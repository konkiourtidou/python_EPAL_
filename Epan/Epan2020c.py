max = -1
for i in range (25,30):
    print i, "/11:"
    ak = raw_input("Enter the vehicle registration number: ")
    sumday = 0
    while ak != "TELOS":
        f = ak[:3]
        print f
        if f == "TAA" or f == "DOK" or f == "KYA":
            print "Free access"
        else:
            if int(ak[6])%2 != i%2:
                print "Fine"
                sumday = sumday + 100
        if sumday > max:
            max = sumday
            maxday = i
        ak = raw_input("Enter the vehicle registration number: ")
    print "Fine of the day:", sumday
print maxday, "/ 11 the day with the most fines"