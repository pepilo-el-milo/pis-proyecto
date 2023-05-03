import os, sys, re

# Validar que se pasen todos los argumentos
if len(sys.argv) < 4:
    print("El programa debe de recibir 3 entradas \n -Modo (tokenize o index) \n -Folder de entrada (Files)\n -Folder de salida (Outputs)")
    exit()

# Definir folders de entrada y salida
folder_path = os.path.join(sys.argv[2], "")
output_path = os.path.join(sys.argv[3])

files = os.listdir(folder_path)

if not os.path.isdir(folder_path):
        print("El folder de entrada proporcionado no existe en el directorio actual.")
        exit()

if not os.path.isdir(output_path):
        os.mkdir(output_path)

ordered_folder = os.path.join(output_path, "ordered")
if not os.path.isdir(ordered_folder):
    os.mkdir(ordered_folder)

# Definición de clase de HashTable y sus métodos
class HashTable:
    def __init__(self, elements):
        self.bucketSize = len(elements)
        self.buckets = [[] for i in range(self.bucketSize)]
        self.assignBuckets(elements)

    def assignBuckets(self, elements):
        for key, value in elements:
            hashedValue = hash(key)
            index = hashedValue % self.bucketSize
            self.buckets[index].append((key, value))

    def getValue(self, input_key):
        hashedValue = hash(input_key)
        index = hashedValue % self.bucketSize
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None
    
    def __str__(self):
        return print.pformat(self.buckets)

# Método para obtener los archivos ordenados
def order():
    for x in files:
        filename = folder_path + x
        f = open(filename, "r",  errors="ignore", encoding="utf8")
        f.read()
        if x.endswith(".html"):
            with open(filename, errors="ignore") as htmlremover:
                y = htmlremover.read()
                y = re.sub("<[^>]*>", "", y)
                splita = re.findall(r'\b\w+\b', y)
                splita = sorted(splita)
                filename_fixed = filename.replace(folder_path, "")
                file_path = os.path.join(ordered_folder, f"ordered_words({filename_fixed}).txt")

                if not os.path.isdir(ordered_folder):
                    os.mkdir(ordered_folder)

                with open(file_path, "w") as f:
                    for y in splita:
                        f.write(y + "\n")

# Método de tokenizar
def tokenize():
    with open(os.path.join(output_path, "tokenizacion.txt"), 'w') as f:
        f.write("Tokenización\nPalabra--#Archivos--Posting\n")
        for bucket in hashtable.buckets:
            if bucket:
                for miniBucket in bucket:
                    word = miniBucket[0]
                    wordData = miniBucket[1]
                    archivos = len(wordData["archivos"])
                    posting = wordData["posting"]
                    f.write(f"{word}--{archivos}--{posting}\n")
            else:
                f.write(f"[Empty Bucket]--[0]--[-1]\n")

# Método de tokenizar e indexar
def index():
    tokenize()
    with open(os.path.join(output_path, "indexacion.txt"), 'w') as f:
        f.write("Indexación\nArchivo--Frecuencia\n")
        for w, pVal in word_dict.items():
            for doc, frec in pVal['archivos'].items():
                f.write(f"{doc}--{frec}\n")

        for bucket in hashtable.buckets:
            if bucket:
                for miniBucket in bucket:
                    wordData = miniBucket[1]
                    for doc, frec in wordData["archivos"].items():
                        f.write(f"{doc}--{frec}\n")
            else:
                f.write(f"[0]--[-1]\n")

# Ordenar archivos y asignarlos en las clase de HashTable
order()

directory = os.listdir(ordered_folder)
word_dict = {}
contPost = 0

for filename in directory:
    if filename.endswith(".txt"):
        filepath = os.path.join(ordered_folder, filename)
        with open(filepath, 'r') as file:
            for line in file:
                words = line.split()
                for w in words:
                    if w not in word_dict:
                        word_dict[w] = {"archivos": {filename: 1}, "posting": 0}
                    else: 
                        if filename not in word_dict[w]["archivos"]:
                            word_dict[w]["archivos"][filename] = 1
                        else:
                            word_dict[w]["archivos"][filename] += 1

for key, value in word_dict.items():
    value['posting'] = contPost
    contPost += len(value['archivos'])

hashtable = HashTable(word_dict.items())

# Direccionar programa dependiendo del modo seleccionado
if sys.argv[1] == "tokenize":
    tokenize()
elif sys.argv[1] == "index":
    index()
else:
    print("El 'Modo' seleccionado es incorrecto.\nSolo puede escoger entre 'tokenize' o 'index'") 