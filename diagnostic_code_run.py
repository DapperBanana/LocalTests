
import xml.etree.ElementTree as ET

def is_valid_xml(xml_str):
    try:
        ET.fromstring(xml_str)
        return True
    except ET.ParseError:
        return False

# Test the function
xml1 = "<note><to>Tove</to><from>Jani</from></note>"
xml2 = "<note><to>Tove</to><from>Jani</from>"
xml3 = "<note><to>Tove<from>Jani</from></note>"

print(is_valid_xml(xml1))  # Output: True
print(is_valid_xml(xml2))  # Output: False
print(is_valid_xml(xml3))  # Output: False
