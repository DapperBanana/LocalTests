
import xml.etree.ElementTree as ET

def is_valid_xml(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except Exception as e:
        return False

xml_string = """
<root>
    <child>test</child>
</root>
"""

if is_valid_xml(xml_string):
    print("The given string is a valid XML document.")
else:
    print("The given string is not a valid XML document.")
