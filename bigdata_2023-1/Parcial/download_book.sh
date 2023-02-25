#!/bin/bash

mkdir -p input

# Especifica la ruta al archivo de texto que contiene los enlaces
links_file_path="links_books_data_set.txt"

# Especifica la ruta al archivo de texto que contiene los nombres de archivo
names_file_path="id_books.txt"

# Abre los archivos de texto para lectura
exec 3<$links_file_path
exec 4<$names_file_path

# Descarga cada archivo con wget
while read link <&3 && read name <&4; do
    wget -O "input/$name" "$link"
done

# Cierra los archivos de texto
exec 3<&-
exec 4<&-

