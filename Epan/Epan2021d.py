def anaz(on, X):
    pos = -1
    i = 0
    while pos == -1 and i <= len(X) - 1:
        if on == X[i]:
            pos = i
        i = i + 1
    return pos
    
XWRA = []
XRYSO = []
ARGYRO = []
XALK = []
for i in range (86):
    print "For the ", i+1, "th country"
    x = raw_input("Enter the name of the country: ")
    XWRA.append(x)
    x = int(input("Enter the number of gold medals: "))
    a = int(input("Enter the number of silver medals: "))
    xa = int(input("Enter the number of bronze medals: "))
    XRYSO.append(x)
    ARGYRO.append(a)
    XALK.append(xa)
max = -1
for m in XRYSO:
    if m > max:
        max = m
print "Countries with maximum number of gold medals: "
for i in range (86):
    if XRYSO[i] == max:
        print XWRA[i]
on = raw_input("Enter the name of a country: ")
pos = anaz(on, XWRA) 
if pos != -1:
    print "Gold: ", XRYSO[pos], " Silver: ", ARGYRO[pos], " Bronze: ", XALK[pos]
else:
    print "The country you entered did not take part in the 2021 Paralympic Games"
