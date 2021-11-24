# Συνάρτηση που ελέγχει αν οι καταθέσεις του m λογαριασμού
# επαρκούν για την ανάληψη poso ευρώ
def money(k,p,m):
    if k[m] >= p:
        flag = True
    else:
        flag = False
    return flag

sumk = 0 #Σύνολο καταθέσεων
suma = 0 #Σύνολο αναλήψεων
lg = int(input("Δώστε αριθμό λογαριασμού ή 0 για τερματισμό: "))
while lg != 0:
    eidos = int(input("Δώστε 1 για κατάθεση ή 2 για ανάληψη: "))
    poso = input("Δώστε ποσό συναλλαγής: ")

    # Δυαδική Αναζήτηση του αριθμού λογαριασμού που πληκτρολογήθηκε (lg)
    # στους υπάρχοντες λογαριασμούς (LOG)
    first = 0
    last = len(LOG)-1
    found = False
    while first <= last and not found:
        mid = (first+last)/2
        if LOG[mid] == lg:
            found = True
        elif LOG[mid] < lg:
            first = mid+1
        else:
            last = mid-1

    # Έλεγχος αν ο λογαριασμός βρέθηκε
    if found:
        print "τρέχον υπόλοιπο", KATATH[mid]
        # Πραγματοποίηση συναλλαγής
        if eidos == 2:
            if money(KATATH, poso, mid):
                KATATH[mid] = KATATH[mid] - poso
                print "Επιτυχής ανάληψη ", poso, " ευρώ"
                suma = suma + poso
            else:
                print "Το τρέχον υπόλοιπο δεν επαρκεί"
        else:
            KATATH[mid] = KATATH[mid] + poso
            print "Επιτυχής κατάθεση ", poso, " ευρώ"
            sumk = sumk + poso
    else:
        print "Ο λογαριασμός που πληκτρολογήσατε δεν υπάρχει"
    lg = int(input("Δώστε αριθμό λογαριασμού ή 0 για τερματισμό: "))

print "Κλείσιμο ταμείου"
print "Σύνολο καταθέσεων: ", sumk, "σύνολο αναλήψεων: ", suma
