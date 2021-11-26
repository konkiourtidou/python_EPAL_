n = int(input("Δώστε αριθμό βαγονιών: "))
QUE = []
v = input("Δώστε όγκο κιβωτίου: ")
while v != 0:
    QUE.append(v)
    v = input("Δώστε όγκο κιβωτίου: ")

w = [0] # όγκος κιβωτίων κάθε βαγονιού
while len(QUE) != 0 and len(w) <= n:
    count = 0 # πλήθος κιβωτίων στο τρέχων βαγόνι
    while len(QUE) != 0 and w[-1] + QUE[0] <= 2000:
        count = count + 1
        x = QUE.pop(0)
        w[-1] = w[-1] + x
    print "Φορτώθηκαν ", count, " κιβώτια με όγκο: ", w[-1]
    w.append(0)
w.pop()

sum = 0
for x in w:
    sum = sum + x

if len(QUE) == 0:
    print "Χρησιμοποιήθηκαν ", len(w), " βαγόνια"
    print "Φορτώθηκαν συνολικά ", sum, " lt"
else:
    print "Παρέμειναν ", len(QUE), " κιβώτια στην αποθήκη"
    print "Δεν αξιοποιήθηκαν ", 2000*n-sum, " lt στα βαγόνια"
