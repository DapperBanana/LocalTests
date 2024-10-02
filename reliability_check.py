
from lxml import etree

def is_valid_xml_with_dtd(xml_string):
    try:
        parser = etree.XMLParser(dtd_validation=True)
        etree.fromstring(xml_string, parser)
        return True
    except etree.XMLSyntaxError:
        return False

# Test the function
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

result = is_valid_xml_with_dtd(xml_string)
if result:
    print("The XML document is valid with a DTD.")
else:
    print("The XML document is not valid with a DTD.")
