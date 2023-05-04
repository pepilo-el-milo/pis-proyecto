import os, time, pprint, json

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
tokens_per_file = {}

#El folder Ordered contiene todos los archivos txt que salen de la Act3 
folder_path = os.path.join(os.path.dirname(__file__), "Ordered")
directory = os.listdir(folder_path)

contPost = 0

end_times = []
for filename in directory:
    s_time = time.time()
    if filename.endswith(".txt"):
        filepath = os.path.join(folder_path, filename)
        tokens_per_file[filename] = 0
        with open(filepath, 'r') as file:
            words_tmp = []
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
                    if w not in words_tmp:
                        words_tmp.append(w)
                        tokens_per_file[filename] += 1
    e_time = time.time()
    end_times.append(e_time - s_time)
    file_time += (e_time - s_time)

for key, value in word_dict.items():
    value['posting'] = contPost
    contPost += len(value['archivos'])

hashtable = HashTable(word_dict.items())

txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
doc_dict = {i: txt_files[i] for i in range(len(txt_files))}

with open("Logs/a11/a11_documents.txt", "w") as f:
    f.write("Act11\nID\tArchivo\n")
    for key, value in doc_dict.items():
        f.write(str(key) + "\t" + value + "\n")

# with open("Logs/a11/a11_posting.txt", 'w') as f:
#     f.write("Act11\nArchivo--Peso\n")
#     for bucket in hashtable.buckets:
#         if bucket:
#             for miniBucket in bucket:
#                 wordData = miniBucket[1]
#                 for doc, frec in wordData["archivos"].items():
#                     tokenCountFile = tokens_per_file[doc]
#                     peso = (frec * 100)/tokenCountFile
#                     f.write(f"{doc}--{frec}--{peso}\n")
#         else:
#             f.write(f"[0]--[-1]\n")

with open("Logs/a11/a11_posting.txt", 'w') as f:
    f.write("Act11\nArchivo--Peso\n")
    for bucket in hashtable.buckets:
        if bucket:
            for miniBucket in bucket:
                wordData = miniBucket[1]
                for doc, frec in wordData["archivos"].items():
                    tokenCountFile = tokens_per_file[doc]
                    for doc_id, filename in doc_dict.items():
                        if filename == doc:
                            doc_key = doc_id
                            break
                    peso = (frec * 100) / tokenCountFile
                    f.write(f"{doc_key}--{frec}--{peso}\n")
        else:
            f.write(f"[0]--[-1]\n")

with open("Logs/a11/a11_dicc.txt", 'w') as f:
    f.write("Act11\nPalabra--#Archivos--Posting\n")
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

exec_time = time.time() - start_time

with open('Logs/a11/a11_matricula.txt', 'w') as f:
    f.write("Act11\n")
    for i in range(len(directory)):
        f.write(f"{directory[i]}    {str(round(end_times[i], 2))} \n")
    f.write(f"\nTiempo total en la lectura de los archivos: {str(round(file_time, 2))} segundos\n")
    f.write(f"Tiempo total de ejecuciÃ³n: {str(round(exec_time, 2))} segundos")