import math
 

factorial_10 = str(math.factorial(10))
with open('/Users/Dubian/OneDrive - UPB/Documentos/dubian/coursera/python/modulo2/ejemplo.txt', 'a') as b_file:
    b_file.write(factorial_10)