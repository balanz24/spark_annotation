import sys
import pandas as pd
import numpy as np

def generate_random_strings(n, length=10):
    return [''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), length)) for _ in range(n)]

def main(csv_filename):
    # Cargar el CSV original
    original_df = pd.read_csv(csv_filename)

    # Crear valores random para las nuevas columnas
    random_values = {
        'name': generate_random_strings(len(original_df)),
        'inchi': generate_random_strings(len(original_df)),
        'inchikey': generate_random_strings(len(original_df))
    }

    # Crear el nuevo DataFrame con las columnas originales y las nuevas columnas random
    new_df = pd.DataFrame({
        'id': original_df['id'],
        'name': random_values['name'],
        'formula': original_df['sf'],  # Asumí que 'formula' es la columna original
        'inchi': random_values['inchi'],
        'inchikey': random_values['inchikey']
    })

    # Obtener el nombre del archivo sin la extensión
    file_name_without_extension = csv_filename.split('.')[0]

    # Generar el nombre del archivo TSV
    tsv_filename = f'{file_name_without_extension}.tsv'

    # Escribir el nuevo DataFrame en un TSV
    new_df.to_csv(tsv_filename, sep='\t', index=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_filename>")
    else:
        csv_filename = sys.argv[1]
        main(csv_filename)
