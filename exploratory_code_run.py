
import xml.etree.ElementTree as ET

def is_valid_xml_with_dtd(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError as e:
        return False

# Sample XML with DTD
xml_with_dtd = """
<!DOCTYPE sample[
<!ELEMENT sample (#PCDATA)>
]>
<sample>Test</sample>
"""

if is_valid_xml_with_dtd(xml_with_dtd):
    print("Valid XML document with DTD")
else:
    print("Invalid XML document with DTD")
