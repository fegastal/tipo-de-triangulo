print("Insira os valores do primeiro lado do triângulo")
l1=float(input())
print("Insira os valores do segundo lado do triângulo")
l2= float(input())
print("Insira os valores do terceiro lado do triângulo")
l3 = float(input())
if ((l1<l2+l3) and (l2<l3+l1) and (l3<l1+l2)):
    print("Teste")
    if ((l1==l2==l3)):
        print("Equilátero")
    else:
        if ((l1==l2 or l2==l3 or l3==l1)):
            print ("Isósceles")
        else:
            print ("Escaleno")