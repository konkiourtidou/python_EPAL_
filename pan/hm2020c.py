def EISITIRIO(e,p):
    kostos = e*10 + p*5
    return kostos

sum = 0
countp = 0
count = 0
print "Διαθέσιμες θέσεις:", 500 - count
en = int(input("Δώστε πλήθος ενηλίκων: "))
while en != -1:
    pai = int(input("Δώστε πλήθος παιδιών: "))
    poso = EISITIRIO(en, pai)
    print "Ωφείλετε: ", poso
    sum = sum + poso
    count = count + en + pai
    countp = countp + pai
    print "Διαθέσιμες θέσεις:", 500 - count
    en = int(input("Δώστε πλήθος ενηλίκων: "))
print "Συνολικά έσοδα: ", sum
pos = countp*100.0/count
print "Ποσοστό παιδιών: ", pos, "%"
