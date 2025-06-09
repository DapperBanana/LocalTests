
import xml.etree.ElementTree as ET

def is_valid_xml_with_dtd(xml_string):
    try:
        root = ET.fromstring(xml_string)
        if root.tag == 'html' and root.get('PUBLIC') is not None:
            return True
        return False
    except ET.ParseError:
        return False

# Input XML string with DTD
xml_string = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>Example</title>
</head>
<body>
<p>Hello, World!</p>
</body>
</html>
"""

if is_valid_xml_with_dtd(xml_string):
    print("The given XML document is valid with a DTD.")
else:
    print("The given XML document is not valid with a DTD.")
