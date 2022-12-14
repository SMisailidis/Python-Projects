a = True
b = False
f = propcalc.formula("(p & q) -> (p -> q)")
print (f.is_satisfiable()) #Η συνάρτηση is_satisfiable ελέγχει αν υπάρχει έστω και μία τιμή TRUE στον πίνακα αληθείας
#f = f & ~f
print(f.is_satisfiable())
print(f.is_contradiction()) #Η συνάρτηση is_contradiction ελέγχει αν είναι αρνητική
#f = f | ~f
print(f.is_tautology())   #SOS