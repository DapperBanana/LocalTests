
from lxml import etree

def is_valid_xml_with_dtd(xml_string):
    try:
        dtd = etree.DTD(xml_string)
        parser = etree.XMLParser(dtd_validation=True)
        etree.fromstring(xml_string, parser)
        return True
    except etree.XMLSyntaxError:
        return False

# Test the program
xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
'''
if is_valid_xml_with_dtd(xml_string):
    print("Valid XML with DTD")
else:
    print("Invalid XML with DTD")
