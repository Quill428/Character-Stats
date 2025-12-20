import random, time
O = 0
while O == 0 or O == 1 :
    for i in range(0,6):
        A=random.randrange(1,7)
        B=random.randrange(1,7)
        C=random.randrange(1,7)
        D=random.randrange(1,7)

        if (A <= B and A <= C and A <= D ):
            print(B+C+D)
            Z=(B+C+D)
            print("#1")

        elif (B <= A and B <= C and B <= D ):
            print(A+C+D)
            Z=(A+C+D)
            print("#2")

        elif (C <= A and C <= B and C <= D ):
            print(A+B+D)
            Z=(A+B+D)
            print("#3")

        elif (D <= A and D <= B and D <= C ):
            print(A+B+C)
            Z=(A+B+C)
            print("#4")

        print (A, B, C, D)
        if i == 0:
            Y = Z
            print("one")
        elif i == 1:
            X = Z
        elif i == 2:
            W = Z
        elif i == 3:
            V = Z
        elif i == 4:
            U = Z
        elif i == 5:
            T = Z

    print(Y,X,W,V,U,T)
    print(Y+X+W+V+U+T)
    if(Y+X+W+V+U+T >= 65):   
        if (O==0):
            M=(Y+X+W+V+U+T)
            N=(Y,X,W,V,U,T)
            O = 1
            print("one done:", M)  
            print()
            print()    
        else:
            P=(Y+X+W+V+U+T)
            Q=(Y,X,W,V,U,T)
            O = 2
            print("two done:", P) 
            print()
            print()
    else:
        print("fail")
        print()
        print()

print(M)
print(N)
print(P)
print(Q)
""" 3 hours total"""