# ΘΕΜΑ Γ  2020
# Στο κέντρο μίας πόλης εφαρμόζεται το μέτρο του δακτυλίου για την κυκλοφορία των οχημάτων. 
# Η πρόσβαση στον δακτύλιο γίνεται με βάση τον αριθμό κυκλοφορίας του οχήματος. Ένας αριθμός
# κυκλοφορίας αποτελείται από 3 γράμματα που ακολουθούνται από 4 ψηφία (π.χ. ΙΖΚ1234). 
# Σύμφωνα με το παραπάνω μέτρο, τις μονές ημέρες επιτρέπεται η πρόσβαση των οχημάτων των 
# οποίων ο αριθμός κυκλοφορίας λήγει σε μονό αριθμό. Αντίστοιχα, τις ζυγές ημέρες κυκλοφορούν
# τα οχήματα των οποίων ο αριθμός κυκλοφορίας λήγει σε ζυγό αριθμό. Η παράβαση του παραπάνω
# μέτρου επιφέρει πρόστιμο 100€. Από το μέτρο του δακτυλίου εξαιρούνται τα οχήματα των οποίων
# ο αριθμός κυκλοφορίας ξεκινά από «ΤΑΑ», «∆ΟΚ» και «ΚΥΑ». 
# Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python, το οποίο: 
# Γ1. Για κάθε ημέρα από τις 25 έως και τις 29 Νοεμβρίου να πραγματοποιεί τα παρακάτω: 
#     α)  Να διαβάζει τον αριθμό κυκλοφορίας του οχήματος που διέρχεται από το σημείο ελέγχου.
#         Η εισαγωγή να τερματίζει όταν δοθεί ως αριθμός κυκλοφορίας η λέξη «ΤΕΛΟΣ» (μον. 4). 
#     β)  Να ελέγχει εάν το όχημα ανήκει στις εξαιρούμενες κατηγορίες εμφανίζοντας κατάλληλο 
#         μήνυμα. Σε διαφορετική περίπτωση να εξετάζει αν υπάρχει παράβαση, εμφανίζοντας το 
#         μήνυμα «ΠΡΟΣΤΙΜΟ» (μον. 9).                                                   Μονάδες 13 
# Γ2. Να υπολογίζει και να εμφανίζει το ποσό των εσόδων από τα πρόστιμα της κάθε ημέρας.Μονάδες 4 
# Γ3. Να εντοπίζει και να εμφανίζει την ημέρα με τα περισσότερα πρόστιμα. Θεωρήστε ότι υπάρχει
#     μόνο μία ημέρα με τα περισσότερα πρόστιμα.                                        Μονάδες 5
# Γ4. Να υπολογίζει και να εμφανίζει το πλήθος των οχημάτων που εξαιρέθηκαν του μέτρου στο 
#     σύνολο των ημερών.                                                                Μονάδες 3


max = -1
for i in range (25,30):
    print i, "/11:"
    ak = raw_input("Enter the vehicle registration number: ")
    sumday = 0
    while ak != "TELOS":
        f = ak[:3]
        print f
        if f == "TAA" or f == "DOK" or f == "KYA":
            print "Free access"
        else:
            if int(ak[6])%2 != i%2:
                print "Fine"
                sumday = sumday + 100
        if sumday > max:
            max = sumday
            maxday = i
        ak = raw_input("Enter the vehicle registration number: ")
    print "Fine of the day:", sumday
print maxday, "/ 11 the day with the most fines"
