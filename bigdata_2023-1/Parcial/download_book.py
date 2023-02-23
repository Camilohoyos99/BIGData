import os
import subprocess

# Especifica la ruta al archivo de texto que contiene los enlaces
links ='https://www.gutenberg.org/ebooks/'
file_path = 'links_books_data_set.txt'

# Especifica el directorio de destino donde se guardarán los archivos descargados
destination_dir = '/home/estudiantes/BIGData/bigdata_2023-1/Parcial'


file_path_id= 'id_books.txt'
with open(file_path_id, 'r') as IDS:
    ids=[]
    for line in IDS:
        line=line[:-2]
        ids.append(line)

# Abre el archivo de texto que contiene los enlaces
print (ids)


with open(file_path, 'r') as file:

    cont=0
    # Lee cada línea del archivo y descarga el archivo correspondiente 
    for link in file:
        
        print("link",link)
        #filename = os.path.basename(line)
        wdet.download(link,destination_dir)
        cont+=1
   
