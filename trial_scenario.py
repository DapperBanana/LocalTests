
from xml.etree import ElementTree as ET

def is_valid_xml_with_dtd(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError as e:
        return False

xml_with_dtd = """
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

xml_without_dtd = """
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
"""

print(is_valid_xml_with_dtd(xml_with_dtd))
print(is_valid_xml_with_dtd(xml_without_dtd))
