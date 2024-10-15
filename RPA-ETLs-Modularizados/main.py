# main.py

from src.etl import ETLProcess

def main():
    csv_path = './data/source/experiencias_por_pais.csv'  # Asegúrate de que esta ruta sea correcta
    target_path = './data/target/'  # Asegúrate de que esta ruta sea correcta
    etl = ETLProcess(csv_path, target_path)
    etl.run()  # Ejecuta el proceso ETL

if __name__ == "__main__":
    main()
