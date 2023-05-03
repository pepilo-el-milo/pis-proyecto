import os, time

start_time = time.time()
file_time = 0

word_dict = {}

#El folder Ordered contiene todos los archivos txt que salen de la Act3 
folder_path = os.path.join(".", "Ordered")
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
                    if w not in word_dict:
                        word_dict[w] = {"repeticiones": 0, "archivos": []}
                    word_dict[w]["repeticiones"] += 1
                    if filename not in word_dict[w]["archivos"]:
                        word_dict[w]["archivos"].append(filename)                 
    e_time = time.time()
    end_times.append(e_time - s_time)
    file_time += (e_time - s_time)

with open("./Logs/a6_result.txt", 'w') as f:
    f.write("Act6\nPalabra--Repeticiones--#Archivos\n")
    for w in word_dict:
        repeticiones = word_dict[w]["repeticiones"]
        archivos = len(word_dict[w]["archivos"])
        f.write(f"{w}--{repeticiones}--{archivos}\n")

exec_time = time.time() - start_time

with open('./Logs/a6_matricula.txt', 'w') as f:
    f.write("Act 6\n")
    for i in range(len(directory)):
        f.write(f"{directory[i]}    {str(round(end_times[i], 2))} \n")
    f.write(f"\nTiempo total en crear los nuevos archivos: {str(round(file_time, 2))} segundos\n")
    f.write(f"Tiempo total de ejecución: {str(round(exec_time, 2))} segundos")