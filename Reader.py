import os
from collections import OrderedDict
from traceback import print_tb
from Vertex import Vertex
from Graph import Graph
from Conecction import Conecction
from random import randrange
import sys

palabras = []
sinrepetir = []
graph = Graph()


class reader():
    path = "C:/Users/Salesianos/Desktop/2ºGS/SGE/songs"
    os.chdir(path)

    def readTextFile(file_path):
        with open(file_path, 'r') as archivo:
            # Línea por línea elimina caracteres especiales y separa palabra por palabra almacenándolas en una tabla
            for lineas in archivo:
                lineas = lineas.replace(",", " ").replace(".", " ").replace("'", "").replace(
                    "()", "").replace("?", "").replace("!", "").replace("'", "").replace("(", "").replace(")", "").lower()
                palabras.extend(lineas.split())

    def createGraph(sinrepetir):
        # Bucle que rellena el graph con los vertex sin repetir palabras
        for i in range(len(sinrepetir)):
            graph.table.append(Vertex(sinrepetir[i]))

    def createConnections(palabras, graph):
        # Bucle que recorre los vertex
        for i in range(len(graph.table)):
            # Bucle que recorre las palabras, sin contar la primera
            for j in range(len(palabras)):
                # Condición para no comparar la primera
                if j > 0:
                    # Guardamos el anterior
                    anterior = palabras[j-1]
                    # Condición que compara la anterior palabra con el vertex actual
                    if anterior == graph.table[i].word:
                        # Bucle que encuentra el vertex a introducir y lo introduce
                        for z in range(len(graph.table)):
                            if graph.table[z].word == palabras[j]:
                                # Condición para la primera vez que iteramos
                                if len(graph.table[i].connections) < 1: 
                                    graph.table[i].connections.append(Conecction(graph.table[z], 1))
                                    break
                                else : 
                                    # Comparamos las conexiones para ver si existe o no
                                    for y in range(len(graph.table[i].connections)):
                                        existe = False
                                        if graph.table[i].connections[y].vertex.word == palabras[j]:
                                            existe = True
                                            break
                                        if existe == True:
                                            graph.table[i].connections[y].peso = graph.table[i].connections[y].peso + 1
                                            break
                                        else:
                                            graph.table[i].connections.append(Conecction(graph.table[z], 1))
                                            break

    def createSongs(graph):
        # Elegimos la palabra con la que empezara la canción
        clave = graph.table[randrange(len(graph.table))]
        print(clave.word)
        for j in range(10):
            print(f"")
            for i in range(10):
                # Opción que crea la canción entre las conexiones disponibles
                random = randrange(len(clave.connections))
                sys.stdout.write(clave.connections[random].vertex.word + " ")
                clave = clave.connections[random].vertex
                # Opción que crea la canción con la conexión con más peso (Problema con el estribillo)
                # for f in range(len(clave.connections)):
                #     pesoComparador = clave.connections[0].peso
                #     if clave.connections[f].peso > pesoComparador:
                #         pesoComparador = clave.connections[f].peso
                #         break
                # for z in range(len(clave.connections)):
                #     if pesoComparador == clave.connections[z].peso:
                #         sys.stdout.write(clave.connections[z].vertex.word + " ")
                #         clave = clave.connections[z].vertex
                #         break

    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path}\{file}"
            readTextFile(file_path)

    sinrepetir = list(OrderedDict.fromkeys(palabras))
    createGraph(sinrepetir)
    createConnections(palabras, graph)
    createSongs(graph)