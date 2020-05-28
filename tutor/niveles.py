infile = open('niveles.txt', 'r')
niv = 0
h = 0
nivel = []
caracteristicas = []
lines = infile.readlines()
nivel.append(int(lines[0]))
numero_de_autos = int(lines[1])
print(numero_de_autos)
for i in range(2,numero_de_autos+2):
    caracteristicas.append(lines[i])
print(caracteristicas)
nivel.append(caracteristicas)
print(nivel)    
#    loncad = len(line)
#    if loncad < 4: # Toma las cadenas , en este caso de numero de coches
 #        i = int(line)
#         print (i)
#         if i != 20:  # Si es distinto de 20 , numero de niveles
#             niv +=1 # Contador de niveles...
#             else:
#    if loncad > 4: # Para las cadenas del coche...
#        for x in range(i):
 #           caracteristicas [i] = line # Aquí recibo el error.
#    nivel [niv] =  caracteristicas # Añado a cada posición de nivel la lista        caracteristicas



#print (nivel)
