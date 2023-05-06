class Ventana:
    __titulo=""
    __x1= int
    __y1= int
    #x1 e y1 son las coordenadas del superior izquierdo
    __x2= int
    __y2= int
    #x2 e y2 son las coordenadas del inferior derecho

    def __init__(self, titulo, x1=0, y1=0, x2=0, y2=0):
        self.__titulo=titulo
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
        self.__validar()

    def __validar(self):
        if (self.__x1 and self.__y1 < 0
            or self.__x2 and self.__y2 > 500
            ): raise ValueError("Puntos invalidos.")

    def getTitulo(self):
        return self.__titulo
	
    def alto(self):
        return self.__y2-self.__y1

    def ancho(self):
        return self.__x2-self.__x1

    def mostrar(self):
         print("\n-Vertices-\n")
         print(f"Superior Izquierdo: ({self.__x1}, {self.__y1})\n")
         print(f"Inferior Derecho: ({self.__x2}, {self.__y2})\n")
    
    def bajar(self, desp=0):
        self.__y1-=desp
        self.__y2-=desp
        self.__validar()

    def subir(self, desp=0):
        self.bajar(-desp) 

    def moverDerecha(self, despl):
        self.__x1+=despl
        self.__x2+=despl
        self.__validar()

    def moverIzquierda(self, despl):
        self.moverDerecha(-despl)