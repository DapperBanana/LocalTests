
import xml.etree.ElementTree as ET

def is_valid_xml_with_dtd(xml_string):
    try:
        parser = ET.XMLParser(dtd_validation=True)
        ET.fromstring(xml_string, parser=parser)
        return True
    except ET.ParseError as e:
        return False

# Test the function with a sample XML string
xml_string = """
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>
"""

if is_valid_xml_with_dtd(xml_string):
    print("The XML document is valid with DTD.")
else:
    print("The XML document is not valid with DTD.")
