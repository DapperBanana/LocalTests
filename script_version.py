
import xml.etree.ElementTree as ET

def is_valid_xml_with_dtd(xml_str, dtd_path):
    try:
        # Parse the XML document
        xml_tree = ET.fromstring(xml_str)
        
        # Parse the DTD document
        dtd_tree = ET.DTD(dtd_path)
        
        # Validate the XML document with the DTD
        is_valid = dtd_tree.validate(xml_tree)
        
        return is_valid
    except ET.ParseError as e:
        print("Error parsing XML:", e)
        return False
    except ET.DTDParseError as e:
        print("Error parsing DTD:", e)
        return False

# Sample XML document
xml_str = """
<!DOCTYPE greeting SYSTEM "greeting.dtd">
<greeting>Hello, world!</greeting>
"""

# Sample DTD document
dtd_path = "greeting.dtd"

# Check if the XML document is valid with the DTD
result = is_valid_xml_with_dtd(xml_str, dtd_path)
if result:
    print("The XML document is valid with the DTD.")
else:
    print("The XML document is not valid with the DTD.")
