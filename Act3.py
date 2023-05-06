import os,time,re

start_time = time.time()
files = os.listdir("Files")
segundosTotales = 0
results_path = os.path.join(os.path.dirname(__file__), "Ordered")

times = []

for x in files:
    filename = "Files/" + x
    f = open(filename, "r",  errors="ignore", encoding="utf8")
    start = time.time()
    f.read()
    end = time.time()
    result = (end - start)
    segundosTotales += result
    times.append(filename + "  " + str(result))
    if x.endswith(".html"):
        with open(filename, errors="ignore") as htmlremover:
            y = htmlremover.read()
            y = re.sub("<[^>]*>", "", y)
            splita = re.findall(r'\b\w+\b', y)
            splita = sorted(splita)
            filename_fixed = filename.replace("Files/", "")
            file_path = os.path.join(results_path, f"ordered_words({filename_fixed}).txt")

            if not os.path.isdir(results_path):
                os.mkdir(results_path)
            
            with open(file_path, "w") as f:
                for y in splita:
                    f.write(y + "\n")

end_time = time.time()
final_time = end_time - start_time

totalTimes = "\nTiempo total en crear el nuevo archivo: " + \
    str(segundosTotales) + " segundos \nTiempo total de ejecución: " + \
    str(final_time) + " segundos"

file_path = "Logs/act3/a3_matricula.txt"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, "w") as file:
    file.write("newfile\n")
    for x in times:
        file.write(x + "\n")
    file.write(totalTimes)