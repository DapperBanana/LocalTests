
import xml.etree.ElementTree as ET

def is_valid_xml(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False

# Test cases
xml_string_1 = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"
xml_string_2 = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</note>"

print(is_valid_xml(xml_string_1))  # Output: True
print(is_valid_xml(xml_string_2))  # Output: False
