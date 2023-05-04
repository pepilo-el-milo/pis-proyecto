import os, sys, time, pprint

# Asegurarse de tener los parámetros deseados
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('El programa debe de recibir 1 entrada: La palabra a buscar')
    exit()

start_time = time.time()
file_time = 0
wordSearch = sys.argv[1]

# Función que regresa True si es que se encontró la palabra en el archivo
def searchFiles(word, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        if word in content:
            return True
        else:
            return False

folder_path = os.path.join(os.path.dirname(__file__), 'Ordered')
directory = os.listdir(folder_path)
results = []
end_times = []

for filename in directory:
    s_time = time.time()
    file_path = os.path.join(folder_path, filename)
    if searchFiles(wordSearch, file_path):
        results.append(filename)
    e_time = time.time()
    end_times.append(e_time - s_time)
    file_time += (e_time - s_time)

exec_time = time.time() - start_time

with open('Logs/a12/a12_results.txt', 'w') as file:
    for index, result in enumerate(results):
        file.write(f'{index+1}. {result}\n')

with open('Logs/a12/a12_matricula.txt', 'w') as f:
    f.write("Act12\n")
    for i in range(len(directory)):
        f.write(f"{directory[i]}    {str(round(end_times[i], 2))} \n")
    f.write(f"\nTiempo total en la lectura de los archivos: {str(round(file_time, 2))} segundos\n")
    f.write(f"Tiempo total de ejecución: {str(round(exec_time, 2))} segundos")