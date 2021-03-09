print("hola alumnos")
print("hola mundo") ; print("adios bbys")
#para ayudarme
nombre = "mi nombre es dubian"
nombre
nombre ="mi nombre es \
    dubian"
nombre
5+6
10%3
10**3
9//2
hola ="""esto es u mensaje 
con tres saltos
de linea """
print(hola)
n1=2
n2=4
if n1<n2:
    print("el numero 2 es mayor")

def mensaje():
    print("hola hola hola")
mensaje()



"listas "

listas = [1,3,"sombrero",1+1]
listas
listas[1]
listas[:]
listas[6]
lista2 = [1,5,7,8,"marrano","cerdo","cochino"]
lista2 [0:4]
lista2 [2:]
lista2 [:4]
lista2.append("puerco")
lista2 
lista2.insert(3,"choncho")
lista2
lista2.extend([0,0,0,0,0,0,0])
lista2
lista2.index(0)
print(0 in lista2)
print("dubian" in lista2)
lista2.remove(0)
lista2
lista2.pop()
lista2

lista3 = ["sandra","lucia"]
lista4 = lista2+lista3
lista4
lista3 = ["sandra","lucia"]*3
lista3

"tuplas"


tupla1 = (1,2,5,7,9)
tupla1
tupla1[2]
lista_t1=list(tupla1)
lista_t1
tupla=tuple(lista_t1)
tupla
print(2 in tupla)
lista2.count(0)
tupla.count(10)
len(lista2)
len(tupla)
tupla2 = ("dubian",)
len(tupla2)
nac = ("dubian", 10 ,3, 1998)
nombre , dia , mes , agno = nac
nombre
dia
mes
agno
nac.index(3)


"diccionarios"

capital = {"colombia": "bogota","argentina":"buenos aires", "cuba": "cuba"}
capital["colombia"]
capital["argentina"]
capital["mexico"]="medellin"
capital
capital["mexico"]="mexico"
capital
del capital["colombia"]
capital
tuplita = ("colombia","eeuu","ecuador")
diccionario = {tuplita[0]:"bogota",tuplita[1]:"washintong",tuplita[2]:"quito"}
diccionario
basquet ={23:"jordan","nombre":"michael","equipo":"chicago","anillos":[1991,1993,1995,1997]}
basquet[23]
basquet["anillos"]
basquet.keys()
basquet.values()
len(basquet)



"condicionales"

"if"

def evaluar(nota):
    valoracion ="aprobado"
    if nota < 5:
        valoracion = "suspendido"
    return valoracion 
evaluar(4)

print("programa de evaluación de notas de alumnos")

nota_alumno = input("introduce la nota del alumno")

def evaluar(nota):
    valoracion ="aprobado"
    if nota < 5:
        valoracion = "suspendido"
    return valoracion 

evaluar(int(nota_alumno))



print("control del edad para las personas")
edad = int(input("dijite su edad : "))

if edad < 18:
    print("puede pasar")
elif edad > 105:
    print("la edad es incorrecta")
else:
    print("no puede pasar")

nota1 = int(input("escriba la nota: "))
if nota1 < 4:
    print("perdio")
elif nota1 < 5:
    print("mejor")
elif nota1 < 7:
    print("paso")
elif nota1 < 9:
    print("super")
else:
    print("eres pro")



"ejercicios"

def DevuelveMax(a,b):
    print(a," es el numero mayor")
DevuelveMax(5,7)

def DevuelveMax(a,b):
    if a>b :
        print(a," es el numero mayor")
    else:
        print(b," es el numero mayor")
DevuelveMax(5,7)


"ejercicio 2"
nombre = input("nombre: ")
apellido = input("apellido: ")
telefono = input("telefono: ")
diccionario = {"Nombre ":nombre, "Apellido":apellido,"Tel":telefono}
print("los datos son: ", diccionario)

"ejercicio 3"

n1 = int(input("escribe primer numero: "))
n2 = int(input("escribe segundo numero: "))
n3 = int(input("escribe tercer numero: "))
print((n1+n2+n3)/3)



"condicionales and. or y in"

edad = 700
if 0<edad <100:
    print("edad correcta")
else:
    print("edad incorrecta")


s1 = 100000
print("el salario del precidente es ",s1)
s2 = 10000
s3 = 1000
s4 = 100

if s1>s2>s3>s4:
    print("el orden es correcto")
else:
    print("el orden es incorrecto")


distancia = 5

hermanos = 7

salario = 10000

if distancia > 40 and hermanos >= 2 and salario < 20000 or salario< 5000:
    print("felicitaciones, optubiste la beca")
else:
    print("no cumples para la beca ")


    "bucles"

for i in ["primavera","verano","otoño"]:
    print("es la ",i," vez que se imprime")

