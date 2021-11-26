sum = 0.0
count = 0
min = 200
for i in range(35):
    on = raw_input("Δώστε όνομα: ")
    prs = 1
    xr = input("Δώστε χρόνο: ")
    while xr > 180 and c <= 4:
        xr = input("Δώστε χρόνο: ")
        prs = prs + 1
    if xr <= 180:
        print on, xr
        count = count + 1
        sum = sum + xr
        if xr < min:
            min = xr
            minon = on
    else:
        print "ΜΗ ΣΥΜΜΕΤΟΧΗ"

mo = sum/count
print "Πλήθος προκτιθέντων: ", count, " με μέσο χρόνο: ", mo
print "Ο ", minon, " είχε τον μικρότερο χρόνο: ", min, "sec"
