# υπολογισμός αθροίσματος
def add():
    ss=a+b	# στη μεταβλητή ss ανατίθεται το άθροισμα των παραμέτρων της συνάρτησης
    return ss	# η συνάρτηση επιστρέφει την τιμή της ss

# υπολογισμός γινομένου
def gin():
    gg=a*b	# στη μεταβλητή gg ανατίθεται το γινόμενο των παραμέτρων της συνάρτησης
    return gg	# η συνάρτηση επιστρέφει την τιμή της gg

# υπολογισμός μέσου όρου
def mo():
    mm=(a+b)/2	# στη μεταβλητή mm ανατίθεται ο μέσος όρος των παραμέτρων της συνάρτησης
    return mm	# η συνάρτηση επιστρέφει την τιμή της mm

# εμφάνιση αποτελεσμάτων
def display():
    print('Αθροισμα =',add())
    print('Γινόμενο =',gin())
    print('Μέσος όρος =',mo())

# Κυρίως πρόγραμμα
print('Υπολογισμός Αθροίσματος, Γινομένου και Μέσου όρου')
print('-------------------------------------------------')
a=int(input('Δώσε έναν αριθμό:'))
b=int(input('Δώσε και άλλον αριθμό:'))
display()	# καλεί τη συνάρτηση display() με ορίσματα τους δύο αριθμούς
























