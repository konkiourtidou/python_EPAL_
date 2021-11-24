OMADES = []
BATHMOI = []
for i in range(100):
    om = raq_input("Δώστε όνομα ομάδας")
    b = int(input("Δώστε βαθμολογία 1 - 100")
    OMADES.append(om)
    BATHMOI.append(b)

#Δημιουργία λιστών με τα στοιχεία των ομάδων που προκρίνονται στην επόμενη φάση
PROK = []
BATHPROK= []
for i in range(100):
    if BATHMOI[i] > 150:
        PROK.append(OMADES[i])
        BATHPROK.append(BATHMOI[i])

# Ταξινόμηση τω προκριθέντων σε φθίνουσα σειρά κατά θαθμολογία και
# σε περίπτωση ισοβαθμίας αλφαβητικά κατά όνομα
for i in rage(len(PROK)-1):
    for j in range(len(PROK)-1, i, -1):
        if BATHPROK[j] > BATHPROK[j-1]:
            BATHPROK[j], BATHPROK[j-1] = BATHPROK[j-1], BATHPROK[j]
            PROK[j], PROK[j-1] = PROK[j-1], PROK[j]
        elif PROK[j] < prok[j-1]:
            PROK[j], PROK[j-1] = PROK[j-1], PROK[j]

# Πλήθος ισοβαθμιών στην πρώτη θέση
count = 0
while count < len(PROK) and BATHPROK[count] = BATHPROK[1]:
    count = count + 1
print count, "ισοβαθμίες στην 1η θέση"
