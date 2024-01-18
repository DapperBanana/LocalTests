
from lxml import etree

def is_valid_xml_with_dtd(xml_string):
    # Parse the XML string
    try:
        parser = etree.XMLParser(dtd_validation=True)
        etree.fromstring(xml_string, parser)
    except etree.XMLSyntaxError:
        return False

    # Validate against the DTD
    try:
        dtd = etree.DTD(etree.parse('example.dtd'))  # Replace 'example.dtd' with your DTD file name or path
        valid = dtd.validate(etree.XML(xml_string))
    except etree.DTDParseError:
        valid = False

    return valid

# XML string to check
xml_string = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE root SYSTEM "example.dtd">
    <root>
        <element>Value</element>
    </root>
'''

# Check if the XML string is valid with a DTD
if is_valid_xml_with_dtd(xml_string):
    print("The XML document is valid with a DTD.")
else:
    print("The XML document is not valid with a DTD.")
