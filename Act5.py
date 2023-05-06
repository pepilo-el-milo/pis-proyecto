import os, sys, time

start_time = time.time()
file_time = 0

if len(sys.argv) < 3:
    print("El programa debe de recibir 2 entradas \n    -Folder de entrada (Files)\n    -Folder de salida (Outputs)")
    exit()

folder_path = os.path.join(sys.argv[1], "")
output_path = os.path.join(sys.argv[2])

if not os.path.isdir(output_path):
        os.mkdir(output_path)

files = os.listdir(folder_path)

def getWords(path):
    with open(path, 'r') as file:
        words = file.read().split()
        words = [word.lower() for word in words]
        return words
    
def getWordCount(word, list):
    count = 0
    for w in list:
        if word == w : count += 1
    return count

end_times = []

for filename in files:
    s_time = time.time()
    file_path = folder_path + filename
    words = getWords(file_path)
    wordsSet = list(set(words))
    wordsSet.sort()
    with open(os.path.join(output_path, filename + ".txt"), 'w') as fol:
        for w in wordsSet:
            i = getWordCount(w, words)
            
            fol.write(f"{w} {str(i)} \n")
    e_time = time.time()
    end_times.append(e_time - s_time)
    file_time += (e_time - s_time)

exec_time = time.time() - start_time

file_path = "Logs/act5/a5_matricula.txt"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, 'w') as f:
    f.write("Act 5\n")
    for i in range(len(files)):
        f.write(f"{files[i]}    {str(round(end_times[i], 2))} \n")
    f.write(f"\nTiempo total en crear los nuevos archivos: {str(round(file_time, 2))} segundos\n")
    f.write(f"Tiempo total de ejecución: {str(round(exec_time, 2))} segundos")