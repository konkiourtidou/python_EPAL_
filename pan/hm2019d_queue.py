# -*- coding: utf-8 -*-

def enqueue(queue, item) :
    queue = queue.append( item )
def dequeue(queue) :
    return queue.pop( 0 )
def isEmpty(queue) :
    return len(queue) == 0
def createQueue( ) :
    return [ ]

QUE = createQueue()
ar_vagoniwn = int(input('Δώσε αριθμό βαγονιών: '))

ogos = input('Δώστε όγκο κιβωτίου ή μηδέν για τερματισμό: ')
while ogos > 0:
    enqueue(QUE, ogos)
    ogos = input('Δώστε όγκο κιβωτίου ή μηδέν για τερματισμό: ')

count_vag = 1 #arithmos vagoniou pou fortonoume
plithos_kivotiwn = 0
sum_ogos = 0
sum_ogos_all = 0
while not isEmpty(QUE) and count_vag <= ar_vagoniwn:
    kivotio = dequeue(QUE)
    if kivotio + sum_ogos <= 2000:
        plithos_kivotiwn += 1
        sum_ogos += kivotio
        sum_ogos_all += kivotio
        print sum_ogos, '----', sum_ogos_all, '------', plithos_kivotiwn
    else:
        print 'Στο βαγόνι ', count_vag, ' φορτώθηκαν ', plithos_kivotiwn, ' με συνολικό όγκο ', sum_ogos
        count_vag += 1
        if count_vag <= ar_vagoniwn:
            sum_ogos = kivotio
            sum_ogos_all += kivotio
            plithos_kivotiwn = 1
            print sum_ogos, '----', sum_ogos_all, '------', plithos_kivotiwn
        else:
            enqueue(QUE, kivotio)
            print 'enqueue'

if isEmpty(QUE):
    print 'Στο βαγόνι ', count_vag, ' φορτώθηκαν ', plithos_kivotiwn, ' με συνολικό όγκο ', sum_ogos
    print 'Φορτώθηκαν όλα τα κιβώτια, με συνολικό όγκο: ', sum_ogos_all, ' σε ', count_vag, ' βαγόνια'
else:
    print 'Δεν φορτώθηκαν ', len(QUE), ' κιβώτια και'
    print 'δεν αξιοποιήθηκαν ', 2000*ar_vagoniwn - sum_ogos_all, ' λίτρα στα βαγόνια'
