
from lxml import etree

def is_valid_xml_with_dtd(xml_string, dtd_string):
    try:
        # Create an ElementTree from the XML string
        tree = etree.fromstring(xml_string)

        # Create a DTD object from the DTD string
        dtd = etree.DTD(dtd_string)

        # Validate the XML document against the DTD
        is_valid = dtd.validate(tree)

        return is_valid
    except etree.XMLSyntaxError:
        return False

# Test the function
xml_string = '''
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>
'''

dtd_string = '''
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
'''

if is_valid_xml_with_dtd(xml_string, dtd_string):
    print("The XML document is valid with DTD.")
else:
    print("The XML document is not valid or does not have a DTD.")
