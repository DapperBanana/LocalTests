
import xml.etree.ElementTree as ET

def is_valid_xml(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False

# Test the function with some xml strings
valid_xml = '<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don\'t forget me this weekend!</body></note>'
invalid_xml = '<note><to>Tove</to><from>Jani><heading>Reminder</heading><body>Don\'t forget me this weekend!</body></note>'

print(is_valid_xml(valid_xml))  # Output: True
print(is_valid_xml(invalid_xml))  # Output: False
