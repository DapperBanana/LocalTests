
import xml.etree.ElementTree as ET

def is_valid_xml(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False

# Test the function
xml_string1 = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"
xml_string2 = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</note>"

if is_valid_xml(xml_string1):
    print("The XML document is valid.")
else:
    print("The XML document is not valid.")

if is_valid_xml(xml_string2):
    print("The XML document is valid.")
else:
    print("The XML document is not valid.")
