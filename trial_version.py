
from xmlschema import XMLSchema

def check_xml_with_dtd(xml_string, dtd_string):
    schema = XMLSchema(dtd_string)
    try:
        schema.validate(xml_string)
        return True
    except Exception as e:
        print(f"Validation error: {e}")
        return False

# Example XML document with DTD
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

# Example DTD
dtd_string = """
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
"""

if check_xml_with_dtd(xml_string, dtd_string):
    print("The XML document is valid with the DTD.")
else:
    print("The XML document is not valid with the DTD.")
