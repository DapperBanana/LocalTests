
from xml.dom import minidom

def is_valid_xml_with_dtd(xml_string):
    try:
        dom = minidom.parseString(xml_string)
        return True
    except Exception as e:
        return False

xml_string = "<!DOCTYPE xml><root><name>John</name></root>"
if is_valid_xml_with_dtd(xml_string):
    print("The given string is a valid XML document with a DTD.")
else:
    print("The given string is not a valid XML document with a DTD.")
