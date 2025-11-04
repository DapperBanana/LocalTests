
from xml.dom import minidom

def is_valid_xml_with_dtd(xml_string):
    try:
        dom = minidom.parseString(xml_string)
        return True
    except Exception as e:
        return False

xml_string = """
<!DOCTYPE note [
    <!ELEMENT note (to,from,heading,body)>
    <!ELEMENT to (#PCDATA)>
    <!ELEMENT from (#PCDATA)>
    <!ELEMENT heading (#PCDATA)>
    <!ELEMENT body (#PCDATA)>
]>
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>
"""

if is_valid_xml_with_dtd(xml_string):
    print("The given XML document is valid with DTD.")
else:
    print("The given XML document is not valid with DTD.")
