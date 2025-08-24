dic = {"n1": "+" , "n2": "-" ,"n3": "*","n4": "/" }
print(dic["n1"])
print(dic["n2"])
print(dic["n3"])
print(dic["n4"])        

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

print("Seleccione la operacion que desea realizar:")
print ("Seleccione la operacion que desea realizar:")
print ("1. Sumar")
print ("2. Restar")
print ("3. Multiplicar")
print ("4. Dividir")
opcion = input("Ingrese su eleccion: ")

if opcion == '1':
    print("El resultado de la suma es:", a + b)
elif opcion == '2':
    print("El resultado de la resta es:", a-b)
elif opcion == '3':
    print("El resultado de la multiplicacion es:", a*b)
elif opcion == '4':
    if b != 0:
        print("El resultado de la division es:", a/b)