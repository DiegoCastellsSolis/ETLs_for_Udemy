# src/xml_generator.py

import xml.etree.ElementTree as ET
from .utils import indent_xml, get_country_code, country_map

def generate_xml_from_df(df, output_file, country):
    """
    Genera un archivo XML a partir de un DataFrame de pandas.

    :param df: DataFrame de pandas que contiene los datos de las experiencias.
    :param output_file: Ruta del archivo XML donde se guardará el resultado.
    :param country: Nombre del país para el cual se generan las experiencias.
    """
    # Crear el elemento raíz
    root = ET.Element('rss', {
        'xmlns:g': 'http://base.google.com/ns/1.0',
        'version': '2.0',
        'xmlns:atom': 'http://www.w3.org/2005/Atom'
    })

    channel = ET.SubElement(root, 'channel')
    title = ET.SubElement(channel, 'title')
    title.text = f'Smartbox - {country}'

    country_name_in_english = country_map.get(country)
    if not country_name_in_english:
        raise ValueError(f"Error: País '{country}' no encontrado en el mapeo.")

    link = ET.SubElement(channel, 'link')
    link.text = generate_link(country_name_in_english)

    description = ET.SubElement(channel, 'description')
    description.text = f'Experiencias disponibles en {country}.'

    for _, row in df.iterrows():
        item = ET.SubElement(channel, 'item')
        ET.SubElement(item, 'id_experiencia').text = str(row['ID de Experiencia'])
        ET.SubElement(item, 'experiencia').text = row['Experiencia']
        ET.SubElement(item, 'categoria').text = row['Categoría']
        ET.SubElement(item, 'ubicacion').text = row['Ubicación']
        ET.SubElement(item, 'pais').text = row['País']
        ET.SubElement(item, 'duracion').text = row['Duración']
        ET.SubElement(item, 'precio').text = str(row['Precio'])
        ET.SubElement(item, 'disponibilidad').text = row['Disponibilidad']

    indent_xml(root)
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

def generate_link(country_name):
    """
    Genera un enlace basado en el nombre del país.

    :param country_name: Nombre en inglés del país.
    :return: Enlace correspondiente.
    """
    country_code = get_country_code(country_name)
    base_url = 'www.bigbox.com' if country_name in ['Uruguay', 'Perú', 'Argentina', 'México'] else 'www.bigbox'
    return f'{base_url}.{country_code.lower()}'
