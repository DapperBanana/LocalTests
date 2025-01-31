
from xml.etree import ElementTree as ET

def is_valid_xml_with_dtd(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False

xml_string = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>Test</title>
</head>
<body>
<h1>Hello, world!</h1>
</body>
</html>
"""

if is_valid_xml_with_dtd(xml_string):
    print("The given string is a valid XML document with a DTD.")
else:
    print("The given string is not a valid XML document with a DTD.")
