a=int(input('Δώσε έναν αριθμό (a):'))
b=int(input('Δώσε και άλλον έναν αριθμό (b):'))
if a>b and a>10:
    print('Το a είναι μεγαλύτερο του b και μεγαλύτερο του 10')
if a>b and not a>10:
    print('Το a είναι μεγαλύτερο του b και μικρότερο ή ίσο του 10')
if not a>b and b==10:
    print('Το a δεν είναι μεγαλύτερο του b και το b είναι 10')
if not a>b and not b==10:
    print('Το a δεν είναι μεγαλύτερο του b και το b δεν είναι 10')
print('Τέλος')








