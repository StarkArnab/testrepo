x=[[0,2],[0,1]]

print("matrix x is:")

for i in range(len(x)):

    print("\t",x[i])

y=[[0,0],[3,4]]

print("matrix y is:")

for i in range(len(y)):

    print("\t",y[i])

def strassen(a,b):

    S=[b[0][1]-b[1][1],

       a[0][0]+a[0][1],

       a[1][0]+a[1][1],

       b[1][0]-b[0][0],

       a[0][0]+a[1][1],

       b[0][0]+b[1][1],

       a[0][1]-a[1][1],

       b[1][0]+b[1][1],

       a[0][0]-a[1][0],

       b[0][0]+b[0][1]]

 

    P=[a[0][0]*S[0],

       S[1]*b[1][1],

       S[2]*b[0][0],

       a[1][1]*S[3],

       S[4]*S[5],

       S[6]*S[7],

       S[8]*S[9]]

 

    C=[[P[4]+P[3]-P[1]+P[5],P[0]+P[1]],

       [P[2]+P[3],

        P[4]+P[0]-P[2]-P[6]]]

 

    print("Strassen's Matrix multiplication of x and y is.")

    print(S)

    print(P)

    print(C)

strassen(x,y)
