
import xml.etree.ElementTree as ET

def is_valid_xml_with_dtd(xml_string):
    try:
        parser = ET.XMLParser(dtd_validation=True)
        root = ET.fromstring(xml_string, parser)
        return True
    except ET.ParseError:
        return False

# Test the function with some sample XML strings
xml_string1 = '''
<!DOCTYPE xml>
<root>
    <child>Some content</child>
</root>
'''
print(is_valid_xml_with_dtd(xml_string1))  # Output: True

xml_string2 = '''
<root>
    <child>Some content</child>
</root>
'''
print(is_valid_xml_with_dtd(xml_string2))  # Output: False
