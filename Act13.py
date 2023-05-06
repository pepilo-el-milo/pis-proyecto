import os, sys, time, pprint

# Asegurarse de tener los parámetros deseados
if len(sys.argv) < 2:
    print('El programa debe de recibir al menos un token de entrada')
    exit()

start_time = time.time()
file_time = 0
wordSearch = sys.argv[1]
sys.argv.pop(0)
words = sys.argv

# Función que regresa True si es que se encontró la palabra en el archivo
def searchFiles(file_path):
    with open(file_path, 'r') as file:
        content = file.read().split("\n")
        count = 0
        for w in words:
            for c in content:
                if w.lower() == c.lower():
                    count += 1
                    break
    return count == len(words)

folder_path = os.path.join(os.path.dirname(__file__), 'Ordered')
directory = os.listdir(folder_path)
results = []
end_times = []

for filename in directory:
    s_time = time.time()
    file_path = os.path.join(folder_path, filename)
    if searchFiles(file_path):
        results.append(filename)
    e_time = time.time()
    end_times.append(e_time - s_time)
    file_time += (e_time - s_time)

exec_time = time.time() - start_time

file_path = "Logs/act13/"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(os.path.join(file_path, "a13_results.txt"), 'w') as file:
    file.write("Retrieve")
    for w in words:
        file.write(f" {w} ")
    file.write("\nTop 10 Documents \n\n")
    for index, result in enumerate(results):
        if index == 10:
            break
        file.write(f'{index+1}. {result}\n')

with open(os.path.join(file_path, "a13_matricula.txt"), 'w') as f:
    f.write("Act13\n")
    for i in range(len(directory)):
        f.write(f"{directory[i]}    {str(round(end_times[i], 2))} \n")
    f.write(f"\nTiempo total en la lectura de los archivos: {str(round(file_time, 2))} segundos\n")
    f.write(f"Tiempo total de ejecución: {str(round(exec_time, 2))} segundos")