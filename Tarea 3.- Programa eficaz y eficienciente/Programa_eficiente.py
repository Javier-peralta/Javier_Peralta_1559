op = "S"
while op == "S":
    try:
        print("ingrese el numero a multiplicar")
        n=float(input())

        print("ingrese hasta que numero quiere realizar la tabla de multiplicar")
        n2=float(input())
        
    except:
        print("Error ingrese un numero valido")
        continue

    for j in range (1,int(n2)+1):
        print(n,"x",j,"=",n*j)


    if op == "S":
        print("¿Desea realizar otra tabla? S/N")
        op=str(input()).upper()

    while op != "N" or op != "S":
        if op == "N":
            break
        
        elif op == "S":
            break
        
        else:  
            print("Entrada invalida intentelo de nuevo \n¿Desea realizar otra tabla? S/N")   
            op=str(input()).upper()
        
