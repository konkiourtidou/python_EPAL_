# ΘΕΜΑ Γ  Επαναληπτικές 2019
# Ένα ξενοδοχείο διαθέτει 50 δωμάτια και λειτουργεί 100 ημέρες τον χρόνο. Θεωρείστε ότι το κόστος
# διανυκτέρευσης είναι 80€ για κάθε δωμάτιο. 
# Να γράψετε πρόγραμμα σε γλώσσα προγραμματισμού Python το οποίο να πραγματοποιεί τα παρακάτω: 
# Γ1. Για κάθε μέρα να διαβάζει το πλήθος των αναχωρήσεων (δωμάτια που αδειάζουν) ελέγχοντας την 
#     εγκυρότητα των δεδομένων, δηλαδή, ότι το πλήθος των αναχωρήσεων είναι μικρότερο ή ίσο από 
#     το πλήθος των κατειλημμένων δωματίων.                                                 Μονάδες 6
# Γ2. Για κάθε μέρα να διαβάζει το πλήθος των αφίξεων (δωμάτια που γεμίζουν) ελέγχοντας την 
#     εγκυρότητα των δεδομένων, δηλαδή, ότι το πλήθος των αφίξεων δεν μπορεί να είναι μεγαλύτερο
#     από το πλήθος των κενών δωματίων.                                                     Μονάδες 6 
# Γ3. Να υπολογίζει και να εμφανίζει το πλήθος των ημερών που το ξενοδοχείο είχε πληρότητα 100%, 
#     δηλαδή και τα πενήντα (50) δωμάτια ήταν κατειλημμένα.                                 Μονάδες 5 
# Γ4. Να υπολογίζει και να εμφανίζει τον μέσο όρο του πλήθους των δωματίων (μέση πληρότητα) που ήταν
#     κατειλημμένα στο διάστημα λειτουργίας των εκατό (100) ημερών.                         Μονάδες 4 
# Γ5. Να υπολογίζει και να εμφανίζει τα συνολικά έσοδα του ξενοδοχείου από τις διανυκτερεύσεις για 
#     το διάστημα λειτουργίας των εκατό (100) ημερών.                                       Μονάδες 4


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
