class Vertice:

    def __init__(self, n):
        self.nombre = n
        self.vecinos = list()
        self.distancia = 9999
        self.color = 'white'
        self.pred = -1

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo:
    def __init__(self):
        self.vertices = dict()

    def agregarVertices(self, vertices):
        for v in vertices:
            n = Vertice(v)
            self.agregarVertice(n)

    def agregarAristas(self, aristas):
        for arista in aristas:
            self.agregarArista(arista[0], arista[1])

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False

    def bfs(self, vert):
        vert = self.vertices[vert]
        vert.distancia = 0
        vert.color = 'gray'
        vert.pred = -1
        q = list()

        q.append(vert.nombre)

        while len(q) > 0:

            u = q.pop()
            node_u  = self.vertices[u]
            for v in node_u.vecinos:
                node_v = self.vertices[v]
                if node_v.color == 'white':
                    node_v.color = 'gray'
                    node_v.distancia = node_u.distancia + 1
                    node_v.pred = node_u.nombre
                    q.append(v)
            self.vertices[u].color = 'black'        

    def imprimeGrafo (self):
        for key in sorted(list(self.vertices.keys())):
            print ("Vertice " + key + " sus vecinos son "+ str(self.vertices[key].vecinos) )
            print("La distancia de A a " + key + " es: "+ str(self.vertices[key].distancia))
            print()



#Creamos un grafo como en tu ejemplo al que llamamos g1:
vertices = [chr(i) for i in range(ord('A'), ord('K'))]
edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ']
g1 = Grafo()
g1.agregarVertices(vertices)
g1.agregarAristas(edges)
g1.bfs('A')


#Creamos otro un grafo al que llamamos g2:
vertices = [chr(i) for i in range(ord('L'), ord('T'))]
edges = ['LM','LP','QT','MJ','NK','OQ','QT','TP']
g2 = Grafo()
g2.agregarVertices(vertices)
g2.agregarAristas(edges)
g2.bfs('L')

#Ahora tenemos dos grafos distintos y podemos trabajar con ellos usando sus nombres, vamos a imprimirlos:
print(print('='*50+'\nGRAFO G1:\n'+'='*50))
g1.imprimeGrafo()

print('='*50+'\nGRAFO G2:\n'+'='*50)
g2.imprimeGrafo()