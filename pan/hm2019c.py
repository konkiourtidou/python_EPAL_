# ΘΕΜΑ Γ  2019
# Σε έναν αγώνα ταχύτητας αυτοκινήτων συμμετέχουν στον προκριματικό 35 οδηγοί με τα αυτοκίνητα τους.
# Στον τελικό αγώνα θα συμμετάσχουν όσοι οδηγοί σημειώσουν επίδοση μικρότερη ή ίση από 180 δευτερόλεπτα
# που αποτελεί το όριο πρόκρισης. Κάθε οδηγός έχει μέχρι τέσσερις (4) προσπάθειες για να πετύχει το όριο
# πρόκρισης. Αν πετύχει σε μία προσπάθεια, σταματά και δεν συνεχίζει τις υπόλοιπες προσπάθειες. 
# Να γράψετε πρόγραμμα σε γλώσσα προγραμματισμού Python, το οποίο: 
# Γ1. Για κάθε οδηγό να διαβάζει το όνομά του (μον. 2) και διαδοχικά τον χρόνο των προσπαθειών του μέχρι
#     να πετύχει την κατάλληλη επίδοση ή να συμπληρωθεί ο αριθμός των προσπαθειών που δικαιούται. (μον. 8) 
#                                                                                                   Μονάδες 10 
# Γ2.  Για κάθε οδηγό να εμφανίζει το όνομά του και αν προκρίθηκε τον χρόνο πρόκρισής του, διαφορετικά να
#      εμφανίζει το μήνυμα “ΜΗ ΣΥΜΜΕΤΟΧΗ”.                                                          Μονάδες 4 
# Γ3. Να υπολογίζει και να εμφανίζει το πλήθος των προκριθέντων οδηγών (μον. 3), καθώς και το μέσο όρο των
#     χρόνων πρόκρισης που πέτυχαν. (μον. 3) Υποθέστε ότι υπάρχει τουλάχιστον ένας.                 Μονάδες 6 
# Γ4. Να βρίσκει και να εμφανίζει το όνομα του οδηγού με το μικρότερο χρόνο πρόκρισης και τον χρόνο αυτό
#     (Υποθέστε ότι είναι μοναδικός).                                                               Μονάδες 5

sum = 0.0
count = 0
min = 200
for i in range(35):
    on = raw_input("Δώστε όνομα: ")
    prs = 1
    xr = input("Δώστε χρόνο: ")
    while xr > 180 and c <= 4:
        xr = input("Δώστε χρόνο: ")
        prs = prs + 1
    if xr <= 180:
        print on, xr
        count = count + 1
        sum = sum + xr
        if xr < min:
            min = xr
            minon = on
    else:
        print "ΜΗ ΣΥΜΜΕΤΟΧΗ"

mo = sum/count
print "Πλήθος προκτιθέντων: ", count, " με μέσο χρόνο: ", mo
print "Ο ", minon, " είχε τον μικρότερο χρόνο: ", min, "sec"
