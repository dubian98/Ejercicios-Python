 "for"
for i in ["dubian","gomez",3]:
    print("hola",end="   ")

for i in "cosas que pasan ":
    print("hola",end="   ")

email = False
for i in "dubian@cosasquepasan":
    if i == "@":
        email=True
if email:
    print("es correcto")
else:
    print("no es correcto")

email2 = True 
mi_i = input("introduce tu email: ")

for i in mi_i:
    if i == "@":
        email2=True
if email2:
    print("es correcto")
else:
    print("no es correcto")v

email2 = 0 
mi_i = input("introduce tu email: ")

for i in mi_i:
    if i == "@" or i ==".":
        email2+=1
if email2==1:
    print("es correcto")
else:
    print("no es correcto")

"range"
for i in range(5):
    print(f"valor de la variable {i}")

for i in range(5,50):
    print(f"valor de la variable {i}")


for i in range(5,50,3):
    print(f"valor de la variable {i}")

len("juan")

v = False
e = input("introduce tu email: ")
for i in range(len(e)):
    if e[i]=="@":
        v=True
if v:
    print("bien")
else:
    print("mal")
len(e)
