class Nodo:
    def __init__(self, nodo, estado, padres, costo, profundidad, camino, test, eFinal):
        self.estado = estado
        self.padres = padres
        self.costo = costo
        self.profundidad = profundidad
        self.camino = camino
        self.test = test
        self.eFinal = eFinal
        self.nodo = nodo

        if eFinal == camino[0]:
            self.test = True

    def __repr__(self):
        return f"Nodo(nodo={self.nodo}, estado={self.estado}, padre = {self.padres} costo={self.costo}, profundidad={self.profundidad}, camino={self.camino}, test={self.test})"

# Ejecución del programa
if __name__ == "__main__":
    #vecinos = [[1 for _ in range(3)] for _ in range(3)]
        
    grafo = [
        [2, 3],  # vecinos de 1 
        [4, 5],  # vecinos de 2
        [6, 7],  # vecinos de 3
        [8, 9],  # vecinos de 4
        [10, 11],  # vecinos de 5
        [12, 13],  # vecinos de 6
        [14, 15],  # vecinos de 7    
    ]
    
    Einit=1
    Efin=8

    cola = [Einit]
    print(cola)
    init = 0
    while init < 10:
        if cola[0] == Efin:
            print("Se encontró NODO con costo = ", init)
            break
        index = cola.pop(0)
        if grafo[index-1][0] != -1:
            cola.append(grafo[index-1][0])
        if grafo[index-1][1] != -1:
            cola.append(grafo[index-1][1])
        print(cola)
        init += 1
    
    vecinos = [
        [2, -1],  # 0 // vecinos de 1
        [1, 3],   # 1 // vecinos de 2
        [2, 4],   # 2 // vecinos de 3
        [3, 5],   # 3 // vecinos de 4
        [4, 6],   # 4 // vecinos de 5
        [5, 7],   # 5 // vecinos de 6
        [6, 8],   # 6 // vecinos de 7
        [7, 9],   # 8 // vecinos de 8
        [8, 10],  # 9 // vecinos de 9
        [9, 11],  # 10 // vecinos de 10
        [10, 12], # 11 // vecinos de 11
        [11, 13], # 12 // vecinos de 12
        [12, 14], # 13 // vecinos de 13
        [13, 15], # 14 // vecinos de 14
        [14, 16], # 15 // vecinos de 15
        [15, 17], # 16 // vecinos de 16
        [16, 18], # 17 // vecinos de 17
        [17, 19], # 18 // vecinos de 18
        [18, -1]  # 19 // vecinos de 19
    ]

    eInicial = 2
    eFinal = 4
    cola = [eInicial]
    padre = []
    numero = 0
    historynodos = []
    nodo_0 = Nodo(numero, estado=eInicial, padres=None, costo=0, profundidad=0, camino=[eInicial], test=False, eFinal=eFinal) 
    historynodos.append(nodo_0)
    print(nodo_0)

    while cola is not None and not nodo_0.test:
        index = cola.pop(0)
        
        if vecinos[index-1][0] != -1:
            cola.append(vecinos[index-1][0])
            padre.append(numero)
        if vecinos[index-1][1] != -1:
            cola.append(vecinos[index-1][1])
            padre.append(numero)
        
        numero += 1  
        #print(padre)       
        myPadre = padre.pop(0)
        
        costo = 0
        for i in historynodos:        
            if(i.nodo == myPadre):
                costo = i.costo + 1
                break
            
        nodos= Nodo(numero, cola[0], myPadre, costo, costo, camino=[eInicial], test=False, eFinal=eFinal)
        nodos.camino.append(nodos.estado)
        historynodos.append(nodos)
        print(nodos)
        
        if cola[0] == eFinal:
            nodo_0.test = True
            
            
