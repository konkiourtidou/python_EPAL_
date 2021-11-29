# ΘΕΜΑ ∆  Επαναληπτικές 2021
# Στους Παραολυμπιακούς Αγώνες που πραγματοποιήθηκαν στο Τόκυο το 2021, συμμετείχαν 86 χώρες. 
# Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python, το οποίο να πραγματοποιεί τα παρακάτω: 
# ∆1. Να διαβάζει το όνομα κάθε χώρας και το πλήθος των χρυσών, αργυρών και χάλκινων μεταλλίων αυτής.
#     Το πλήθος των μεταλλίων μπορεί να είναι μηδέν. Τα στοιχεία να καταχωρίζονται στις λίστες XWRA,
#     XRYSO, ARGYR και XALK αντίστοιχα.                                                    Μονάδες 5 
# ∆2. Να υπολογίζει και να εμφανίζει τα ονόματα των χωρών της λίστας XWRA που έχουν κατακτήσει τον
#     μέγιστο αριθμό χρυσών μεταλλίων.                                                     Μονάδες 7 
# ∆3. Να διαβάζει το όνομα μίας χώρας και να εμφανίζει το πλήθος των χρυσών, αργυρών και χάλκινων
#     μεταλλίων που αυτή κατέκτησε. Αν η χώρα δεν υπάρχει στη λίστα XWRA, να εμφανίζει κατάλληλο 
#     μήνυμα. Η αναζήτηση της χώρας να γίνεται με κλήση της συνάρτησης anaz, όπως περιγράφεται στο
#     ερώτημα ∆4.                                                                          Μονάδες 5 
# ∆4. Να υλοποιήσετε τη συνάρτηση με όνομα anaz, η οποία να δέχεται το όνομα της χώρας και τη λίστα
#     XWRA και να επιστρέφει τη θέση στην οποία βρίσκεται η χώρα αυτή στη λίστα XWRA, διαφορετικά να
#     επιστρέφει την τιμή -1.                                                              Μονάδες 8


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
