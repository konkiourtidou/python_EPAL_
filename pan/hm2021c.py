def TYPOS_EMB(age): # Τύπος εμβολίου ανάλογα με την ηλικία (age)
    if age <= 50:
        x = "1"
    elif age <= 60:
        x = "2"
    elif age <= 70:
        x = "3"
    else:
        x = "4"
    x = "Τύπος "+x
    return x

max = 0 # μέγιστη ηλικία
countg = 0 # πλήθος γυναικών
count = 0 # πλήθος όλων
age = int(input("Δώστε ηλικία: "))
while age >= 40:
    f = raw_input("Δώστε φύλο Α/Γ: ")
    while f != "Α" and f != "Γ":
        f = raw_input("Δώστε φύλο Α/Γ: ")
    amka = raw_input("Δώστε AMKA: ")
    t = TYPOS_EMB(age)
    print "Ο/Η ασφαλισμένος/η με ΑΜΚΑ: ", amka, " θα κάνει ",t
    count = count + 1
    if age > max:
        max = age
        maxf = f
        maxAMKA = amka
    if f == "Γ":
        countg = countg + 1
    age = int(input("Δώστε ηλικία: "))
pososto = 100.0*countg/count
print maxf, maxAMKA
print "Γυναίκες: ", pososto, "%"
