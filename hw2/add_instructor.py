import sys
from lxml import etree as ET

xml_path = 'hw2.xml'

def add_instructor(instructor_id, instructor_name, department):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except ET.XMLSyntaxError as e:
        print(f"Error parsing XML file: {e}")
        sys.exit(1)

    new_instructor = ET.Element('instructor', {'id': instructor_id})

    name_element = ET.Element('name')
    name_element.text = instructor_name
    new_instructor.append(name_element)

    department_element = ET.Element('department')
    department_element.text = department
    new_instructor.append(department_element)

    root.find('.//instructors').append(new_instructor)  # Using XPath for finding instructors

    tree.write(xml_path, pretty_print=True, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 add_instructor.py <instructor_id> <instructor_name> <department>")
        sys.exit(1)

    instructor_id, instructor_name, department = sys.argv[1], sys.argv[2], sys.argv[3]
    
    add_instructor(instructor_id, instructor_name, department)

    print(f"Instructor {instructor_id} added successfully.")
