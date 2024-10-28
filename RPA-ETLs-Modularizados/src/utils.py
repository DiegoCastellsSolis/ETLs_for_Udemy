# src/utils.py

import xml.etree.ElementTree as ET
import pycountry

def indent_xml(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent_xml(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def get_country_code(country_name):
    country_obj = pycountry.countries.get(name=country_name)
    if not country_obj:
        raise ValueError(f"País '{country_name}' no encontrado en pycountry.")
    return country_obj.alpha_2

country_map = {
    'Argentina': 'Argentina',
    'Uruguay': 'Uruguay',
    'Chile': 'Chile',
    'Perú': 'Peru',
    'Bolivia': 'Bolivia',
    'México': 'Mexico' 
}
