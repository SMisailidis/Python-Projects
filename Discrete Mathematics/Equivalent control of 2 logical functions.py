print("Έλεγχος ισοδυναμίας 2 λογικών συναρτήσεων:\n")

f = propcalc.formula(" p -> (q -> r)") #Αλλάζουμε τις συναρτήσεις ανάλογα την άσκηση SOS
g = propcalc.formula("(p & q) -> r")
print ("f == g", (f==g))