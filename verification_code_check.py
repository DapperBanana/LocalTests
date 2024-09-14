
import xml.etree.ElementTree as ET

def is_valid_xml(xml_str):
    try:
        ET.fromstring(xml_str)
        return True
    except ET.ParseError:
        return False

# Test the function with a sample XML string
xml_string = '<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don\'t forget me this weekend!</body></note>'
if is_valid_xml(xml_string):
    print("The given string is a valid XML document.")
else:
    print("The given string is not a valid XML document.")
