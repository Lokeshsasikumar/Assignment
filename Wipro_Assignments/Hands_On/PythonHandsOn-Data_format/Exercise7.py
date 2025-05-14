#Exercise 7: Reading XML from String

import xml.etree.ElementTree as ET

def parse_xml():
    xml_data = '''
    <person>
        <name>John</name>
        <age>30</age>
        <city>New York</city>
    </person>'''
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    for child in root:
        print(child.tag, child.text)

parse_xml()
