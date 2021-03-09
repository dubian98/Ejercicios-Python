 x = 1+4*3+8/2*4+5**2
 if x % 2 == 0:
     x += 1
     print(x)
else:
    x += 2
    print(x)


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