import json

def convertStr(s):
    try:
        ret = int(s)
    except ValueError:
        #Try float.
        ret = float(s)
    return ret

def readJSONfile(json_file):
    try:
        with open(json_file, 'r') as f: # abrimos el archivo en solo lectura
            return json.load(f)

    except IOError:
        print 'Problemas con el archivo'
        return 0


## Definimos la funcion de Main del programa
def GDFtoJSON(gdf_file, json_file):
    graph = {}  # Contiene el JSON con el grafo
    nodes = []  # alamcena la lista de nodos
    links = []  # alamacena la lista de aristas
    try:
        with open(gdf_file, 'r') as fp:
            fp.readline()   # Para saltarnos la primera linea
            line = fp.readline()
            while (not ('edgedef>' in line)):  # Buscamos en todas la lineas disponibles en el documento

                try:
                    d = {}
                    data = line.split(',')
                    d['ID'] = data[0]
                    d['Name'] = data[2]
                    d['Category'] = data[3]
                    d['Post_activity'] = convertStr(data[4])
                    d['Fan_count'] = convertStr(data[5])
                    d['Talking_about_count'] = convertStr(data[6])
                    d['Link'] = data[8].rstrip('\n')
                    nodes.append(d)  # Guardamos el nodo en la lista
                    line = fp.readline()  # Pasamos a la siguiente linea

                except:
                    commmaFoundFlag = False
                    x = list(line)
                    index = x.index('"') + 1
                    while True:
                        if x[index] == ',':
                            x[index] = ''
                            commmaFoundFlag = True

                        if (x[index] == '"' and commmaFoundFlag):
                            line = "".join(x)
                            break
                        index = index + 1

            graph['nodes'] = nodes
            fp.readline()  # Saltamos la linea


            while(line):    # Buscamos las aristas del grafo
                d = {}
                data = line.split(',')
                d['Source'] = data[0]
                d['Target'] = data[1]
                d['Directed'] = (False, True)[data[2].rstrip('\n') in data[2]]
                links.append(d)
                line = fp.readline()

            graph['links'] = links

        # Guardamos el grafo resultane en un nuevo archivo
        with open(json_file, 'w') as f:
            f.write(json.dumps(graph, sort_keys=False, indent=2))   # le damos formato en el documento resultante

    except IOError:
        print 'Problemas con el archivo'


