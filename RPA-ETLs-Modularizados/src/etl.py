# src/etl.py

import pandas as pd
from .xml_generator import generate_xml_from_df

class ETLProcess:
    def __init__(self, csv_path, target_path):
        self.csv_path = csv_path
        self.target_path = target_path

    def run(self):
        df = self.extract_data()
        self.load_data(df)

    def extract_data(self):
        """Carga los datos desde un archivo CSV."""
        df = pd.read_csv(self.csv_path)
        return df

    def load_data(self, df):
        """Carga los datos en archivos XML según el país."""
        paises = df['País'].unique()
        for pais in paises:
            country_df = df[df['País'] == pais]
            output_file = f'{self.target_path}{pais}.xml'
            generate_xml_from_df(country_df, output_file, pais)
