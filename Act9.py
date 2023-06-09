import os, time

start_time = time.time()
file_time = 0
contPost = 0
word_dict = {}
stoplist = []

# Obtener listado de palabras baneadas
with open("stoplist.txt", 'r') as file:
    for line in file:
        words = line.split()
        for w in words:
            stoplist.append(w)

#El folder Ordered contiene todos los archivos txt que salen de la Act3 
folder_path = os.path.join(os.path.dirname(__file__), "Ordered")
directory = os.listdir(folder_path)

end_times = []
for filename in directory:
    s_time = time.time()
    if filename.endswith(".txt"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r') as file:
            for line in file:
                words = line.split()
                for w in words:
                    if (w not in stoplist) and (len(w) > 1):
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

for key, value in list(word_dict.items()):
    if len(word_dict[key]["archivos"]) < 2:
        del word_dict[key]

for key, value in word_dict.items():
    value['posting'] = contPost
    contPost += len(value['archivos'])

file_path = "Logs/act9/"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(os.path.join(file_path,"a9_dicc.txt"), 'w') as f:
    f.write("Act9\nPalabra--#Archivos--Posting\n")
    for w in word_dict:
        archivos = len(word_dict[w]["archivos"])
        posting = word_dict[w]["posting"]
        f.write(f"{w}--{archivos}--{posting}\n")

with open(os.path.join(file_path,"a9_posting.txt"), 'w') as f:
    f.write("Act9\nArchivo--Frecuencia\n")
    for w, pVal in word_dict.items():
        for doc, frec in pVal['archivos'].items():
            f.write(f"{doc}--{frec}\n")

# with open("a9_dicc.txt", 'w') as f:
#     f.write("Act9\nPalabra--#Archivos\n")
#     for w in word_dict:
#         archivos = word_dict[w]["archivos"]
#         f.write(f"{w}--{archivos}\n")

exec_time = time.time() - start_time

with open(os.path.join(file_path,"a9_matricula.txt"), 'w') as f:
    f.write("Act9\n")
    for i in range(len(directory)):
        f.write(f"{directory[i]}    {str(round(end_times[i], 2))} \n")
    f.write(f"\nTiempo total en la lectura de los archivos: {str(round(file_time, 2))} segundos\n")
    f.write(f"Tiempo total de ejecuciÃ³n: {str(round(exec_time, 2))} segundos")