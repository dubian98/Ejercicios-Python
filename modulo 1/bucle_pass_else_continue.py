"continue, pass y else"
for letra in "python":
    print("la letra es: ",letra)

"continue"
for letra in "python":
    if letra=="h":
        continue
    print("la letra es: ",letra)

nombre = "pildoras informaticas"
len(nombre)
contador =0
for i in nombre:
    if i==" ":
        continue
    contador +=1
print(contador)

"pass"

while True:
    pass
class miclase:
    pass #ára implementar mas tarde


#else , se ejecuta cuando se acaba de recorrer el bucle 
arroba=False
email =input("introduce tu email please: ")
for i in email:
    if i == "@":
        arroba= True
        break;
else:
    arroba=False
print(arroba)
