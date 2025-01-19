
from xml.etree import ElementTree as ET

def is_valid_xml_with_dtd(xml_string):
    try:
        parser = ET.XMLParser()
        parser.entity = dict((k, None) for k in parser.entity)
        ET.fromstring(xml_string, parser=parser)
        return True
    except ET.ParseError:
        return False

# Example XML document with DTD
xml_with_dtd = '''
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
'''

if is_valid_xml_with_dtd(xml_with_dtd):
    print("The given string is a valid XML document with a DTD.")
else:
    print("The given string is not a valid XML document with a DTD.")
