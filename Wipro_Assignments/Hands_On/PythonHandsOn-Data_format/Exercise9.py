#Exercise 9: Parsing XML from File

import xml.etree.ElementTree as ET

def parse_xml_from_file():
    tree = ET.parse('person.xml')
    root = tree.getroot()

    for child in root:
        print(child.tag, child.text)

parse_xml_from_file()
