import os, time

start_time = time.time()

files = os.listdir("Files")

segundosTotales = 0

times = []

for x in files:
    filename = "Files/" + x
    f = open(filename, "r",  errors="ignore")
    start = time.time()
    f.read()
    end = time.time() 
    result = (end - start)
    segundosTotales += result
    times.append(filename + "  " + str(result))

end_time = time.time()
final_time = end_time - start_time


file_path = "Logs/act1/a1_matricula.txt"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

totalTimes = "\nTiempo total en abrir los archivos:  " + str(segundosTotales) + " segundos \nTiempo total de ejecución: " + str(final_time) + " segundos"

with open(file_path, "w") as file:
    file.write("Act 1\n")
    for x in times:
        file.write(x + "\n")
    file.write(totalTimes)