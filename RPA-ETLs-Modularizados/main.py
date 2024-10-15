# main.py

from src.etl import extract_data, transform_data, load_data

def main():
    csv_path = './data/source/experiencias_por_pais.csv'
    target_path = './data/target/'

    # Etapa de extracción
    df = extract_data(csv_path)

    # Etapa de transformación
    unique_countries = transform_data(df)

    # Etapa de carga
    load_data(df, target_path)

if __name__ == '__main__':
    main()
