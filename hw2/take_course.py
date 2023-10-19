import sys
from lxml import etree as ET

xml_path = 'hw2.xml'

def entity_exists(entities, attribute, value):
    return any(entity.attrib.get(attribute) == value for entity in entities)

def take_course(student_id, course_number, semester):
    try:

        tree = ET.parse(xml_path)
        root = tree.getroot()
    except ET.XMLSyntaxError as e:
        print(f"Error parsing XML file: {e}")
        sys.exit(1)

    # Check if the student, course, and semester exist in the database
    students = root.find('.//students')
    courses = root.find('.//courses')

    student_exists = entity_exists(students, 'id', student_id)
    # Use case-insensitive comparison for course number
    course_exists = entity_exists(courses, 'number', course_number.upper().replace(" ", ""))
    semester_exists = any(course.find('.//semester').text == semester for course in courses)

    if not (student_exists and course_exists and semester_exists):
        print("Error: Student, course, or semester not found in the database.")
        sys.exit(1)

    # Create a new relationship element
    new_relationship = ET.Element('take_course')

    # Add sub-elements for relationship details
    student_id_element = ET.Element('student_id')
    student_id_element.text = student_id
    new_relationship.append(student_id_element)

    course_number_element = ET.Element('course_number')
    course_number_element.text = course_number.upper().replace(" ", "")
    new_relationship.append(course_number_element)

    semester_element = ET.Element('semester')
    semester_element.text = semester
    new_relationship.append(semester_element)

    # Add the new relationship to the root
    root.find('.//take_course').append(new_relationship)

    # Save the modified XML back to the file
    tree.write(xml_path)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python3 take_course.py <student_id> <course_number> <semester>")
        sys.exit(1)

    # Extract command-line arguments
    student_id, course_number, semester = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to establish a relationship
    take_course(student_id, course_number, semester)

    print(f"Student {student_id} takes course {course_number} in {semester} successfully.")

