# ΘΕΜΑ ∆  Επαναληπτικές  2019
# Μία τράπεζα, για τις ανάγκες εξυπηρέτησης των πελατών της, διατηρεί δύο παράλληλες ταξινομημένες 
# λίστες κατά αύξουσα σειρά με βάση τον αριθμό λογαριασμού. Μία λίστα με όνομα LOG[ ], η οποία 
# περιλαμβάνει τους αριθμούς λογαριασμών των πελατών της, και μία λίστα με όνομα KATATH[ ], η οποία 
# περιλαμβάνει το υπόλοιπο του λογαριασμού κάθε πελάτη. Θεωρείστε ότι όλοι οι αριθμοί λογαριασμών 
# που υπάρχουν στη λίστα LOG[ ] είναι μοναδικοί θετικοί ακέραιοι. 
# Η τράπεζα επιθυμεί να γνωρίζει το ύψος των καταθέσεων και των αναλήψεων που πραγματοποιήθηκαν κατά
# τη διάρκεια λειτουργίας του ταμείου. 
# Να γράψετε τμήμα προγράμματος και τις απαραίτητες συναρτήσεις σε γλώσσα προγραμματισμού Python που
# να πραγματοποιεί τα παρακάτω: 
# ∆1. Να διαβάζει για κάθε αιτούμενη συναλλαγή τον αριθμό λογαριασμού, το είδος της συναλλαγής 
#     (1-κατάθεση, 2-ανάληψη) και το ποσό συναλλαγής. Η επαναληπτική διαδικασία  τερματίζεται (κλείσιμο
#     του ταμείου), όταν δοθεί ως αριθμός λογαριασμού ο αριθμός μηδέν (0).                      Μονάδες 3
# ∆2. Να αναζητά τον αριθμό λογαριασμού στη λίστα LOG[ ] και να εμφανίζει το τρέχον υπόλοιπό του από τη
#     λίστα KATATH[ ].                                                                          Μονάδες 7 
# ∆3. Να υλοποιήσετε συνάρτηση money(), η οποία θα καλείται σε περίπτωση που η αιτούμενη συναλλαγή είναι
#     ανάληψη, ώστε να ελέγξει αν επαρκεί το υπόλοιπο του λογαριασμού για να πραγματοποιηθεί η συναλλαγή.
#     Αν το υπόλοιπο επαρκεί, να γίνεται η ανάληψη, σε διαφορετική περίπτωση να ενημερώνεται ο πελάτης με
#     κατάλληλο μήνυμα. Αν η αιτούμενη συναλλαγή είναι κατάθεση, να πραγματοποιείται η συναλλαγή. 
#                                                                                               Μονάδες 10 
# ∆4. Να υπολογίζει και να εμφανίζει το άθροισμα των καταθέσεων και των αναλήψεων, μετά το κλείσιμο του 
#     ταμείου.                                                                                  Μονάδες 5
# Σημείωση:  ∆εν απαιτούνται έλεγχοι ορθότητας δεδομένων. 


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
