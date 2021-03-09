a_file = open('/Users/Dubian/OneDrive - UPB/Documentos/dubian/coursera/python/modulo2/ejemplo.txt', 'r')
a_file.read()    
a_file.close()

with open('/Users/Dubian/OneDrive - UPB/Documentos/dubian/coursera/python/modulo2/ejemplo.txt', 'r') as b_file:
    print(b_file.read())

with open('/Users/Dubian/OneDrive - UPB/Documentos/dubian/coursera/python/modulo2/ejemplo.txt', 'r') as b_file:
    print(b_file.readlines())
with open('/Users/Dubian/OneDrive - UPB/Documentos/dubian/coursera/python/modulo2/ejemplo.txt', 'r') as b_file:
    for line in b_file:
        print(line)
with open('/Users/Dubian/OneDrive - UPB/Documentos/dubian/coursera/python/modulo2/ejemplo.txt', 'w') as b_file:
    b_file.write("hola mundo")
with open('/Users/Dubian/OneDrive - UPB/Documentos/dubian/coursera/python/modulo2/ejemplo.txt', 'w') as b_file:
    b_file.writelines(['hola mundo.\n', 'hola planeta.\n', 'hola tierra.\n'])
with open('/Users/Dubian/OneDrive - UPB/Documentos/dubian/coursera/python/modulo2/ejemplo.txt', 'a') as b_file:
    b_file.writelines(['hola mundo.\n', 'hola planeta.\n', 'hola tierra.\n'])