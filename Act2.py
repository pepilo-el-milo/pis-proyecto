import os, time, re

start_time = time.time()
files = os.listdir("Files")
segundosTotales = 0
tagRegex = re.compile(r'<[^>]+>')
results_path = os.path.join(os.path.dirname(__file__), "Results")

times = []

def tagCleaner(f):
    filename = f.name.replace("Files/", "")
    raw_html = f.read()
    clean_html = re.sub(tagRegex, '', raw_html)
    file_path = os.path.join(results_path, f"remove_html_tags({filename}).html")

    if not os.path.isdir(results_path):
        os.mkdir(results_path)
        
    with open(file_path, "w") as f:
        f.write(clean_html)


for x in files:
    filename = "Files/" + x
    f = open(filename, "r",  errors="ignore")
    start = time.time()
    tagCleaner(f)
    end = time.time() 
    result = (end - start)
    segundosTotales += result
    times.append(filename + "  " + str(round(result, 2)))
    ## print(filename + "  " + str(round(result, 2)))

final_time = time.time() - start_time
## print("Tiempo total en abrir los archivos:  " + str(round(segundosTotales, 2)) + " segundos")
## print("Tiempo total de ejecución: " + str(round(final_time, 2)) + " segundos")

with open("Logs/a2_matricula.txt", "w") as f:
    f.write("Act 2\n")
    for x in times:
        f.write(x + "\n")
    f.write(f"\nTiempo total en abrir los archivos: {str(round(segundosTotales, 2))} segundos\n")
    f.write(f"Tiempo total de ejecución: {str(round(final_time, 2))} segundos")