# ΘΕΜΑ Γ  2021
# Ο σχεδιασμός ενός εμβολιαστικού κέντρου σ’ ένα νησί  για τον μήνα Ιούλιο δίνεται από τον παρακάτω πίνακα:  
# Τύπος Εμβολίου          Ηλικία
#    Τύπος 1        Από 40 έως και 50
#    Τύπος 2        Από 51 έως και 60
#    Τύπος 3        Από 61 έως και 70
#    Τύπος 4            Άνω των 70
# Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python το οποίο να πραγματοποιεί τα παρακάτω:
# Γ1. Να διαβάζει για κάθε ασφαλισμένο που πρόκειται να εμβολιαστεί:
#     * Την ηλικία (ακέραια τιμή). 
#     * Το φύλο ("Α" για άνδρες και "Γ" για γυναίκες) και να κάνει έλεγχο ορθότητας τιμών για το φύλο του κάθε ασφαλισμένου. 
#     * Τον ΑΜΚΑ (Αριθμός Μητρώου Κοινωνικής Ασφάλισης) ως συμβολοσειρά. 
#     Η εισαγωγή των στοιχείων να τερματίζεται, όταν δοθεί ηλικία μικρότερη του 40. Θεωρήστε ότι στο εμβολιαστικό κέντρο
#     ο πρώτος ασφαλισμένος που θα προσέλθει είναι από 40 ετών και πάνω.                                        Μονάδες 6 
# Γ2.  Να καλεί συνάρτηση με όνομα  TYPOS_EMB, η οποία να δέχεται την ηλικία του ασφαλισμένου και να επιστρέφει τον τύπο
#      του εμβολίου σύμφωνα με τον παραπάνω πίνακα (μον. 2). Να αναπτύξετε τη συνάρτηση που χρειάζεται για τον σκοπό αυτό
#      (μον. 4).                                                                                                Μονάδες 6
# Γ3. Να εμφανίζει, με κατάλληλο μήνυμα,  τον ΑΜΚΑ του ασφαλισμένου και τον τύπο του εμβολίου που προκύπτει από τη συνάρτηση. 
#                                                                                                               Μονάδες 2 
# Γ4. Να βρίσκει και να εμφανίζει το φύλο και τον ΑΜΚΑ του ατόμου με τη μεγαλύτερη ηλικία που πρόκειται να εμβολιαστεί
#     (Υποθέστε ότι είναι μοναδική).                                                                            Μονάδες 6 
# Γ5. Να υπολογίζει και να εμφανίζει το ποσοστό των γυναικών στο σύνολο των ασφαλισμένων που πρόκειται να εμβολιαστούν. 
#                                                                                                               Μονάδες 5
    

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
