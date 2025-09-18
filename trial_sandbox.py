
from lxml import etree

def is_valid_xml_with_dtd(xml_string):
    try:
        parser = etree.XMLParser(dtd_validation=True)
        etree.fromstring(xml_string, parser)
        return True
    except Exception as e:
        return False

# Test the program
xml_string_with_dtd = """
<!DOCTYPE note [
    <!ELEMENT note (to,from,heading,body)>
    <!ELEMENT to (#PCDATA)>
    <!ELEMENT from (#PCDATA)>
    <!ELEMENT heading (#PCDATA)>
    <!ELEMENT body (#PCDATA)>
]>
<note>
    <to>You</to>
    <from>Me</from>
    <heading>Hello</heading>
    <body>Just saying hi!</body>
</note>
"""

xml_string_without_dtd = """
<note>
    <to>You</to>
    <from>Me</from>
    <heading>Hello</heading>
    <body>Just saying hi!</body>
</note>
"""

print("Is valid XML with DTD:", is_valid_xml_with_dtd(xml_string_with_dtd))
print("Is valid XML without DTD:", is_valid_xml_with_dtd(xml_string_without_dtd))
