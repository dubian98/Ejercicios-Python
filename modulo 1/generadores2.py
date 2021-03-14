"generadores un * significa que puede recibir varios argumentosn en una tupla"

def dev_ciudades(*ciudades):
    for elementos in ciudades:
        #for subelemento in elementos:
            yield from elementos

ciudades_devueltas = dev_ciudades("medellin","barranquilla","bogota","cartagenta")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
