#Exercise 8: Writing XML to File

import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_and_write_xml():
    person = ET.Element("person")
    name = ET.SubElement(person, "name")
    name.text = "John"
    age = ET.SubElement(person, "age")
    age.text = "30"
    city = ET.SubElement(person, "city")
    city.text = "New York"

    xml_str = ET.tostring(person)
    pretty_xml = minidom.parseString(xml_str).toprettyxml()
    with open("person.xml", "w") as f:
        f.write(pretty_xml)

create_and_write_xml()
