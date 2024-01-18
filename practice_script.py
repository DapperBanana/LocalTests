
from lxml import etree

def is_valid_xml_with_dtd(xml_str):
    try:
        parser = etree.XMLParser(dtd_validation=True)
        etree.fromstring(xml_str, parser)
        return True
    except etree.XMLSyntaxError:
        return False

# Example XML string with a DTD
xml_string = '''
<!DOCTYPE root [
  <!ELEMENT root (child1,child2)>
  <!ELEMENT child1 (#PCDATA)>
  <!ELEMENT child2 (#PCDATA)>
]>
<root>
  <child1>Text 1</child1>
  <child2>Text 2</child2>
</root>
'''

if is_valid_xml_with_dtd(xml_string):
    print("The XML string is valid with DTD.")
else:
    print("The XML string is not valid with DTD.")
