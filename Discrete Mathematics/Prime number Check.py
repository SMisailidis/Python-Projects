print("Έλεγχος πρώτου αριθμού:\n");

def isprime_3(n):
    if n<=1:
        return False
    t = 2
    while t*t <= floor(n): 
        if mod(n,t) == 0:
            return t, False
        t = t+1
    return n, True
    
#Ως παράμετρο, καταχωρήστε τον αριθμό που θέλετε
print (isprime_3(10))
print (isprime_3(131))