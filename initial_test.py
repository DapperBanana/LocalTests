
import xml.etree.ElementTree as ET

def is_valid_xml(input_string):
    try:
        ET.fromstring(input_string)
        return True
    except ET.ParseError:
        return False

# Test the function
xml_string = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"
if is_valid_xml(xml_string):
    print("The input string is a valid XML document.")
else:
    print("The input string is not a valid XML document.")
