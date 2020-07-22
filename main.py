
def generador(y,x):
    """ Generando de la matriz """
    matriz = []
    for k in range(y):
        matriz.append([])
    for i in range(y):
        for j in range(x):
            matriz[i].append(int(input("a_" + str(i+1) + str(j+1) + " = ")))
        print("*"*60)
    return matriz

matriz = generador(3, 3)
total = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[1][0]*matriz[2][1]*matriz[0][2] + matriz[2][0]*matriz[0][1]*matriz[1][2]
total= total+(matriz[0][2]*matriz[1][1]*matriz[2][0])*-1 + (matriz[1][2]*matriz[2][1]*matriz[0][0])*-1 + (matriz[2][2]*matriz[0][1]*matriz[1][0])*-1

if total!=0:
   print (' ',(matriz[1][1]*matriz[2][2]-matriz[2][1]*matriz[1][2])/total,' ',((matriz[0][1]*matriz[2][2]-matriz[2][1]*matriz[0][2])*-1)/total,' ',(matriz[0][1]*matriz[1][2]-matriz[1][1]*matriz[0][2])/total)
   print (' ',((matriz[1][0]*matriz[2][2]-matriz[2][0]*matriz[1][2])*-1)/total,' ',((matriz[0][0]*matriz[2][2]-matriz[2][0]*matriz[0][2]))/total,' ',((matriz[0][0]*matriz[1][2]-matriz[1][0]*matriz[0][2])*-1)/total)
   print (' ',((matriz[1][0]*matriz[2][1]-matriz[2][0]*matriz[1][1]))/total,' ',((matriz[0][0]*matriz[2][1]-matriz[2][0]*matriz[0][1])*-1)/total,' ',(matriz[0][0]*matriz[1][1]-matriz[1][0]*matriz[0][1])/total)
  
else:
    print ("Error el determinante dá 0");

