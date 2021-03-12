"bucle while(sintaxis)"

i=1
while i<=10:
    print(f"{i} entrada")
    i+=1


"2"
edad = int(input("what old are you?: "))

while edad < 0 or edad > 100:
    print("has introducido una edad incorrecta, vuelve a intentar")
    edad = int(input("what old are you?: "))
print("Puede continuar")
print("edad del estudiantes: ",edad," años")

"3"
print("programa de calculo de raiz cuadrada")
import math
numero =int(input("introduce un numero: "))
intentos = 0
while numero < 0 :
    print("no se puede hallar raiz de un numero negativo en los reales")
    if intentos == 4:
        print("has intentado muchas veces ")
        break;
    numero =int(input("introduce un numero: "))
    intentos += 1
if intentos<5:
    solucción = math.sqrt(numero)
    print("la raiz cuadrada es ",solucción)


