import os
import subprocess

# Especifica la ruta al archivo de texto que contiene los enlaces
links ='https://www.gutenberg.org/ebooks/'
file_path = 'id_books.txt'

# Especifica el directorio de destino donde se guardarán los archivos descargados
destination_dir = 'Users/prestamour/Documents/BIGData-main/bigdata_2023-1/Parcial'

# Abre el archivo de texto que contiene los enlaces
with open(file_path, 'r') as file:
    
   
    # Lee cada línea del archivo y descarga el archivo correspondiente
    for line in file:
        # Elimina cualquier espacio en blanco al final de la línea
        link = links + str(line)
        print(link)
        filename = os.path.basename(line)
        subprocess.run(['wget', link, '-O', filename])
   
