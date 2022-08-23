
class Lexico:
    def __init__(self, cadena: str):
        self.cadena = cadena
        self.reservadas = ["def", "if", "else", "elif", "while", "for", "in", "range", ":", "(", ")", "print", "from", "import", "str", "__init__"]
        self.operadoresAritmeticos = ["+", "-", "/", "*", "=", "//", "%"]
        self.operadoresBooleanos = ["and", "or", ">=", "<=", "<", ">", "==", "True", "False"]
        self.resultado=[]
    
    def deslex(self):
        lista = cadenaALista(self.cadena)
        visitadas = []
        for elemento in lista:
            if elemento not in visitadas:
                if(elemento in self.reservadas):
                    print("Reservada: ", elemento)
                    
                elif elemento == "    ":
                    print("Identación: `    `")
    
                elif(elemento in self.operadoresAritmeticos):
                    print("Operador aritmético: ", elemento)
    
                elif(elemento in self.operadoresBooleanos):
                    print("Operador booleano: ", elemento)
                
                elif(elemento.isdigit()):
                    print("Numero: ", elemento)
                
                else:
                    print("Identificador: ", elemento)
                
                visitadas.append(elemento)
                
    def leerArchivo(self, file):
        f = open(file, "r")

        self.cadena = f.read()
        print(self.cadena)

        f.close()
        
def cadenaALista(cadena:str) -> list:
    lista = []

    if(cadena.find("    ")> 0):
        lista.append("    ")

    cad = cadena.split()
    
    bandera = False
    
    for palabra in cad:
        if(palabra.find("(") > 0):
            if(palabra.find(")") > 0):
                lista.extend(palabra.split("("))
                lista.extend(lista.pop().split(","))
                lista.extend(lista.pop().split(")"))
                bandera = True        
        else:
            lista.append(palabra)
    
    for i in range(len(lista)):
        if(lista[i].find(":") > 0):
            lista[i] = lista[i].replace(":", "")
        if(lista[i].find(")") > 0):
            lista[i] = lista[i].replace(")", "")

    if bandera:
        lista.append("(")
        lista.append(")")

    return lista


lex = Lexico("")

lex.leerArchivo("tradu.txt")

lex.deslex()

