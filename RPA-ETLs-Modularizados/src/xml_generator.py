# src/xml_generator.py

import xml.etree.ElementTree as ET
from .utils import indent_xml, get_country_code, country_map

def generate_xml_from_df(df, output_file, country):
    root = ET.Element('rss')
    root.set('xmlns:g', 'http://base.google.com/ns/1.0')
    root.set('version', '2.0')
    root.set('xmlns:atom', 'http://www.w3.org/2005/Atom')

    channel = ET.SubElement(root, 'channel')
    title = ET.SubElement(channel, 'title')
    title.text = f'Smartbox - {country}'

    country_name_in_english = country_map.get(country)
    if not country_name_in_english:
        print(f"Error: País '{country}' no encontrado en el mapeo.")
        return

    link = ET.SubElement(channel, 'link')
    country_code = get_country_code(country_name_in_english)
    link.text = f'www.bigbox.com.{country_code.lower()}' if country in ['Uruguay', 'Perú', 'Argentina', 'México'] else f'www.bigbox.{country_code.lower()}'

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
