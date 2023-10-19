import sys
from lxml import etree as ET

xml_path = 'hw2.xml'

def add_student(student_id, student_name, program):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except ET.XMLSyntaxError as e:
        print(f"Error parsing XML file: {e}")
        sys.exit(1)

    new_student = ET.Element('student', {'id': student_id})

    name_element = ET.Element('name')
    name_element.text = student_name
    new_student.append(name_element)

    program_element = ET.Element('program')
    program_element.text = program
    new_student.append(program_element)

    root.find('.//students').append(new_student)  # Using XPath for finding students

    tree.write(xml_path, pretty_print=True, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 add_student.py <student_id> <student_name> <program>")
        sys.exit(1)

    student_id, student_name, program = sys.argv[1], sys.argv[2], sys.argv[3]

    add_student(student_id, student_name, program)

    print(f"Student {student_id} added successfully.")
