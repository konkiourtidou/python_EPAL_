# -*- coding: utf-8 -*-

# Ένα ηλεκτρονικό κατάστημα καταγράφει τις πωλήσεις των προϊόντων του στο τέλος της ημέρας. 
# Κάθε προϊόν χαρακτηρίζεται από έναν κωδικό. Ο κωδικός αποτελείται από δύο (2) κεφαλαία γράμματα, 
# τα οποία αντιστοιχούν στην χώρα παραγωγής του προϊόντος, και ακολουθείται από οκτώ (8) ψηφία. 
# Ο κωδικός έχει την παρακάτω δομή (ενδεικτικά): GR12467078
# Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python το οποίο:
# Δ1. Για κάθε προϊόν:
# α) Να διαβάζει τον κωδικό του και να τον καταχωρίζει σε λίστα με όνομα CODE (μον.3).
# β) Να διαβάζει την τιμή πώλησης του προϊόντος (μον. 1).
# γ) Να διαβάζει το πλήθος των τεμαχίων που πωλήθηκαν (μον. 1).
# Η εισαγωγή των στοιχείων θα τερματίζεται, όταν δοθεί ως κωδικός προϊόντος η λέξη "ΤΕΛΟΣ".
# Θεωρήστε ότι καταχωρίζονται τουλάχιστον δύο προϊόντα με μη μηδενικές τιμές πώλησης και μη μηδενικό πλήθος τεμαχίων. Μονάδες 5
# Δ2. Να υπολογίζει το ποσό των εσόδων για κάθε προϊόν και να το καταχωρίζει σε λίστα με όνομα ESODA. Μονάδες 3
# Δ3. Να διαβάζει τον κωδικό ενός προϊόντος και να εμφανίζει τα έσοδα από τις πωλήσεις του. Αν ο κωδικός δεν υπάρχει στη λίστα CODE, να εμφανίζει
#     κατάλληλο μήνυμα. Η αναζήτηση του κωδικού να γίνεται με κλήση της συνάρτησης anazitisi, όπως περιγράφεται στο ερώτημα Δ4. Μονάδες 5
# Δ4. Να υλοποιήσετε τη συνάρτηση με όνομα anazitisi, η οποία να δέχεται τον κωδικό του προϊόντος και τη λίστα CODE, και να επιστρέφει τη θέση στην
#     οποία βρίσκεται ο κωδικός στη λίστα CODE, διαφορετικά να επιστρέφει την τιμή ‐1. Μονάδες 6
# Δ5. Να υπολογίζει και να εμφανίζει το ποσοστό των εσόδων των ελληνικών προϊόντων, των οποίων ο κωδικός αρχίζει με GR, στο σύνολο των εσόδων όλων
#     των προϊόντων. Μονάδες 6

def anazitisi(L, key):
    pos = -1
    N = len(L) - 1
    i = 0
    while i <= N and pos < 0:
        if L[i] == key:
            pos = i
        i = i + 1
    return pos

CODE = []
ESODA = []
cod = raw_input('Δώστε κωδικό - δύο γράμματα και οκτώ ψηφία - ή ΤΕΛΟΣ για τερματισμό')
while cod != 'ΤΕΛΟΣ':
    CODE.append(cod)
    timi = float(input('Δώσε την τιμή του προϊόντος: '))
    temaxia = int(input('πόσα τεμάχια: '))
    poso = timi * temaxia
    ESODA.append(poso)
    cod = raw_input('Δώστε κωδικό - δύο γράμματα και οκτώ ψηφία - ή ΤΕΛΟΣ για τερματισμό')

cod = raw_input('Δώστε έναν κωδικό - δύο γράμματα και οκτώ ψηφία ')
thesi = anazitisi(CODE, cod)
if thesi == -1:
    print 'Δεν υπάρχει αυτός ο κωδικός!'
else:
    print ESODA[thesi]

sum_all = 0
sumGR = 0.0
for i in range len(CODE):
    sum_all += ESODA[i]
    if CODE[i][:2] == 'GR':  #ή  'GR' in CODE[i]
        sumGR +=ESODA[i]
pos = sumGR / sum_all * 100
print 'Ποσοστό εσόδων από ελληνικά προϊόντα: ',pos, '%'
