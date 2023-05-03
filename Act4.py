import os, time

start_time = time.time()
folder_path = os.path.join(os.path.dirname(__file__), "Results")
files = os.listdir(folder_path)
segundosTotales = 0
times = []
wordArray = []

def getWords(path):
    with open(path, 'r') as file:
        words = file.read().split()
        words = [word.lower() for word in words]
        return words

for filename in files:
    file_path = os.path.join(folder_path, filename)
    start = time.time()
    words = getWords(file_path)
    end = time.time() 
    result = (end - start)
    segundosTotales += result
    times.append(filename + "  " + str(round(result, 2)))
    wordArray += words

wordArray.sort()

with open('./Logs/a4_results.txt', 'w') as f:
    for word in wordArray:
        f.write(word + '\n')

final_time = time.time() - start_time

with open("./Logs/a4_matricula.txt", "w") as f:
    f.write("Act 4\n")
    for x in times:
        f.write(x + "\n")
    f.write(f"\nTiempo total en crear el nuevo archivo: {str(round(segundosTotales, 2))} segundos\n")
    f.write(f"Tiempo total de ejecución: {str(round(final_time, 2))} segundos")