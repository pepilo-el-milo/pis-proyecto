import os, time, pprint

# Clase HashTable
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
        return pprint.pformat(self.buckets)

start_time = time.time()
file_time = 0

word_dict = {}

#El folder Ordered contiene todos los archivos txt que salen de la Act3 
folder_path = os.path.join(os.path.dirname(__file__), "Ordered")
directory = os.listdir(folder_path)

contPost = 0

end_times = []
for filename in directory:
    s_time = time.time()
    if filename.endswith(".txt"):
        filepath = os.path.join(folder_path, filename)
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
    e_time = time.time()
    end_times.append(e_time - s_time)
    file_time += (e_time - s_time)

for key, value in word_dict.items():
    value['posting'] = contPost
    contPost += len(value['archivos'])

hashtable = HashTable(word_dict.items())

# Iterar sobre valores en Hashtable
# for bucket in hashtable.buckets:
#     if bucket:
#         for miniBucket in bucket:
#             word = miniBucket[0]
#             wordData = miniBucket[1]
#             archivos = len(wordData["archivos"])
#             posting = wordData["posting"]
#             print(f"Palabra: {word}, Archivos: {archivos}, Posting: {posting}")
#     else:
#         print(f"Palabra:    , Archivos: 0, Posting: -1")

file_path = "Logs/act8/"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(os.path.join(file_path,"a8_dicc.txt"), 'w') as f:
    f.write("Act8\nPalabra--#Archivos--Posting\n")
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

with open(os.path.join(file_path,"a8_posting.txt"), 'w') as f:
    f.write("Act8\nArchivo--Frecuencia\n")
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

# with open("a8_dicc.txt", 'w') as f:
#     f.write("Act8\nPalabra--#Archivos\n")
#     for bucket in hashtable.buckets:
#         if bucket:
#             for miniBucket in bucket:
#                 word = miniBucket[0]
#                 wordData = miniBucket[1]
#                 archivos = wordData["archivos"]
#                 f.write(f"{word}--{archivos}\n")
#         else:
#             f.write(f"[0]--[-1]\n")

exec_time = time.time() - start_time

with open(os.path.join(file_path,"a8_matricula.txt"), 'w') as f:
    f.write("Act8\n")
    for i in range(len(directory)):
        f.write(f"{directory[i]}    {str(round(end_times[i], 2))} \n")
    f.write(f"\nTiempo total en la lectura de los archivos: {str(round(file_time, 2))} segundos\n")
    f.write(f"Tiempo total de ejecuciÃ³n: {str(round(exec_time, 2))} segundos")