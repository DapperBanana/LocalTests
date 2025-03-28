
import xml.etree.ElementTree as ET

def is_valid_xml(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False

# Test the function with some examples
xml_string1 = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"
xml_string2 = "<note><to>Tove<from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"

print(is_valid_xml(xml_string1))  # Output: True
print(is_valid_xml(xml_string2))  # Output: False
