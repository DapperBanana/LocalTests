
import xml.etree.ElementTree as ET

def is_valid_xml(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False

# Test the function
xml_string1 = "<root><child>hello</child></root>"
xml_string2 = "<root><child>hello</child>"
xml_string3 = "<root>"
xml_string4 = "invalid xml"

print(is_valid_xml(xml_string1))  # True
print(is_valid_xml(xml_string2))  # False
print(is_valid_xml(xml_string3))  # False
print(is_valid_xml(xml_string4))  # False
