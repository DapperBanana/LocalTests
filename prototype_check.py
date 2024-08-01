
from lxml import etree

def is_valid_xml(xml_string):
    try:
        etree.fromstring(xml_string)
        return True
    except etree.XMLSyntaxError:
        return False

# Test the function
xml_string = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"
if is_valid_xml(xml_string):
    print("The given string is a valid XML document.")
else:
    print("The given string is not a valid XML document.")
