
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError


def is_valid_xml_with_dtd(xml_string):
    try:
        parser = ET.XMLParser(dtd_validation=True)
        ET.fromstring(xml_string, parser=parser)
        return True
    except ParseError as e:
        print("Error:", e)
        return False


# Test the program with some sample XML strings
xml_string_1 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
  <head>
    <title>Sample XML Document</title>
  </head>
  <body>
    <p>This is a sample XML document.</p>
  </body>
</html>
"""
print("XML String 1:", is_valid_xml_with_dtd(xml_string_1))

xml_string_2 = """
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
"""
print("XML String 2:", is_valid_xml_with_dtd(xml_string_2))
