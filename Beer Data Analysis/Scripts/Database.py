import pymongo


class MongoDatabase:
    """
        Crea la conexion con la base de datos de MongoDB.
    """

    def __init__(self, url, database_name):
        try:
            client = pymongo.MongoClient(url)
            self.database = client[database_name]

        except Exception:
            print ("Probles connecting the Database (Invalid URL or Network Timeout).")

        return

    def fetch_collection(self, collection):
        """

        :param collection: Nombre de la coleccion de documentos.
        :return: Lista de diccionarios con todos los documentos de la coleccion.
        """
        data_collection = []
        collection = self.database[collection]
        cursor = collection.find({})
        for document in cursor:
            data_collection.append(document)
        return data_collection

    def load_document(self, collection, json_document):
        """
            Guarda un documento en una coleccion dada.

        :param collection: Nombre de la coleccion de documentos.
        :param json_document: Documento formato JSON que se guardara.
        :return:
        """
        collection = self.database[collection]
        collection.insert_one(json_document)
        return

    def drop_collection(self, collection):
        collection = self.database[collection]
        collection.drop()
        return

    @staticmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def load_csv_file(self, csv_file, setname, init_line, final_line):
        """
        Carga un archivo .CSV en la base de datos

        :param csv_file: Archivo CSV con el que se trabajara
        :param setname: Nombre de la colleccion donde se guardara
        :param init_line: linea donde se comenzara a procesar
        :param final_line: Linea donde se deentra la funcioon.
        :return: None
        """
        # Se cargaron hasta los 32
        import csv

        with open(csv_file, 'rU') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            line_count = 0
            labels = []

            for row in csv_reader:
                if line_count == 0:  # Primero registramos los nombres de las columnas del CSV
                    for i in range(len(row)):
                        labels.append(row[i])
                    line_count += 1

                else:
                    dictionary = {}
                    if line_count >= init_line + 1:
                        for i in range(len(row)):
                            try:
                                if MongoDatabase.is_number(row[i]):
                                    dictionary[labels[i]] = float(row[i])
                                else:
                                    dictionary[labels[i]] = u"" + (row[i].encode("latin1"))

                            except UnicodeDecodeError:
                                dictionary[labels[i]] = "N/A"
                        self.load_document(setname, dictionary)
                        print dictionary['Name'], " Added to the Database... (ID: ", line_count - 1, ")"
                    line_count += 1

                if line_count == final_line + 1:
                    break
            csv_file.close()
        return
