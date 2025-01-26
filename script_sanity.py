
import xml.etree.ElementTree as ET

def is_valid_xml(xml_str):
    try:
        ET.fromstring(xml_str)
        return True
    except ET.ParseError:
        return False

# Test cases
xml_str = '<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don\'t forget me this weekend!</body></note>'
print(is_valid_xml(xml_str))  # Output: True

xml_str_invalid = '<note><to>Tove</from><from>Jani</from><heading>Reminder</heading><body>Don\'t forget me this weekend!</body></note>'
print(is_valid_xml(xml_str_invalid))  # Output: False
