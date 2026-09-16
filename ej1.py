#Ejercicio 7
n= int(input("Introduce un numero: " ))
suma =0.0
for i in range(1,n+1):
    suma += 1/i
print(f"El resultado de la suma es: {suma}")

#Ejercicio 8
n= int(input("Introduce un numero: " ))
resta=0.0
for i in range(1,n+1):
    if i % 2 !=0:
        resta -= 1/i
    else:
        resta += 1/i
print(f"El resultado de la resta es: {resta}")

#Ejercicio 10
n= int(input("Introduce un numero: " ))
for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    print()
#Ejercicio 11
n= int(input("Introduce un numero: " ))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()
#Ejercicio 12


