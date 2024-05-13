
import xml.etree.ElementTree as ET

def check_valid_xml(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False

xml_string = '<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don\'t forget me this weekend!</body></note>'
result = check_valid_xml(xml_string)

if result:
    print("The given string is a valid XML document.")
else:
    print("The given string is not a valid XML document.")
