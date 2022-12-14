
# 1 Array
A = Matrix([[1, 3, 1],
           [2, 2, -5],
           [-3, 2, 8]])
A
print("Ο πινακας ειναι:")
show(A)
print("Ο γραμμο-χωρος του πινακα ειναι:")
show(A.row_space())
print("Ο στηλο-χωρος του πινακα ειναι:")
show(A.column_space())
print("Ο μηδενο-χωρος του πινακα ειναι:")
show(A.right_kernel())
print( "Τα διαγώνια στοιχεία είναι:", A.diagonal() )
print("Η κλιμακωτη του μορφη ειναι:")
show(A.echelon_form())
print ("Η ανηγμενη κλιμακωτη μορφη του ειναι:")
show(A.rref())
print ("Ο βαθμος του πινακα ειναι:")
show(rank(A))
print("Η οριζουσα του πινακα ειναι:")
show(A.det())
print("Ο αναστροφος του πινακα ειναι:")
A2 = A.transpose()
show(A2)
print("Ο γραμμο-χωρος του αναστροφου πινακα ειναι:")
show(A2.row_space())
print("Ο στηλο-χωρος του αναστροφου πινακα ειναι:")
show(A2.column_space())
print("Ο μηδενο-χωρος του πινακα ειναι:")
show(A2.right_kernel())
print( "Τα διαγώνια στοιχεία είναι:", A2.diagonal() )
print("Η κλιμακωτη μορφη του αναστροφου ειναι:")
show(A2.echelon_form())
print("Η ανηγμενη κλιμακωτη μορφη του αναστροφου ειναι:")
show(A2.rref())
print("Η οριζουσα του αναστροφου πινακα ειναι:")
show(A2.det())
print("Ο αντίστροφος του πινακα ειναι:")
A3=A.inverse()
show(A3)
print("Η κλιμακωτη μορφη του αντιστροφου:")
show(A3.echelon_form())
print("Η ανηγμενη κλιμακωτη μορφη του αντιστροφου:")
show(A3.rref())
print("Η οριζουσα του αντιστροφου πινακα ειναι:")
show(A3.det())

#2 arrays
A = matrix([[1, 3, 1], [2, 2, -5],[-3, 2, 8]])

B = matrix([[1, 2, 1],[0, 2, -5],[-3, 7, 2]])

print("Το αθροισμα των πινακων ειναι:")
X=A+B
show(X)

print("Το ευθυ αθροισμα των πινακων ειναι:")
E=A.block_sum(B)
show(E)

print("Το γινομενο των πινακων ειναι:")
C=A*B
show(C)

print("Το γινομενο HADAMARD των πινακων ειναι:")
H=A.elementwise_product(B)
show(H)

print("Το γινομενο KRONECKER των πινακων ειναι:")
K=A.tensor_product(B)
show(K)

#1 Array and 1 vector
A=matrix([[1,2,1,4],
          [2,0,4,3],
          [4,2,2,1],
          [-3,1,3,2]])

b=vector([13,28,20,6])
show(A)
show(b)

print("O επαυξημενος πινακας:")
e=A.augment(b)
show(e)

x=A.solve_right(b)
print("Λυση του συστηματος της μορφης Αx=b")

print("Tα x ειναι:")
show(x)

P,L,U=A.LU(); P^-1,L,U
print("Η LU παραγοντοποιηση του πινακα ειναι:")
print("O πινακας L:")
show(L)
print("O πινακας U:")
show(U)

print("O μοναδιαιος πινακας που χρησιμοποιηθηκε:")
show(P)

#2 Vectors
v=vector([-1,0,1])
u=vector([1,2,3])
show(v)
print("Ο διανυσματικος χωρος στον οποιο ανηκει το διανυσμα:")
x=v.parent()
show(x)

print("Ο διανυσματικος χωρος που παραγεται απο τα u,v:")
S=span([u,v])
show(S)

#3 Vectors
v1=vector([2,3,-1])
v2=vector([2,1,2])
v3=vector([4,3,1])

u1=vector([1,1,1])
u2=vector([0,1,1])
u3=vector([0,0,1])

R=column_matrix([v1,v2,v3])
show(R)
print("rank:");show(rank(R))

S=column_matrix([u1,u2,u3])
show(S)
print("rank:");show(rank(S))
print("O Πινακας SR:")
SR=S.augment(R)
show(SR)

print("Ο γραμμο ισοδυναμος του:")
SR.rref()
show(SR)

print("Ο πινακας μεταβασης:")
M=S^-1*R
show(M)

#4 Vectors
v1=vector([1,1,1,1])
v2=vector([-1,-1,1,1])
v3=vector([-1,1,-1,1])
v4=vector([-1,1,1,-1])

V=matrix([v1,v2,v3,v4])

show(V)
M=V.T*V
show(M)
print("ΚΑΝΟΝΙΚΟΠΟΙΗΣΗ:")
u1=v1/norm(v1)
u2=v2/norm(v2)
u3=v3/norm(v3)
u4=v4/norm(v4)
U=matrix([u1,u2,u3,u4])
show(U)
Y=U.T*U
show(Y)

#1 Array vol2
A=matrix([[5,2,1,0],[2,5,0,1],[1,0,5,2],[0,1,2,5]])
show(A)
print("Tο χαρακτηριστικο πολυωνυμο του πινακα ειναι:")
P=charpoly(A)
show(P)

print("Οι ιδιοτιμες ειναι:")
R=A.eigenvalues()
show(R)

print("Οι ιδιοχωροι:")
X=A.eigenspaces_right()
show(X)