import sys
from lxml import etree as ET

xml_path = 'hw2.xml'

def find_instructor_courses(instructor_id):
    try:
        # Load the existing XML file
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except ET.XMLSyntaxError as e:
        print(f"Error parsing XML file: {e}")
        sys.exit(1)

    # Uses the findall method to locate all <teach_course> elements for the specified instructor ID
    # Then iterates over these elements to extract information about each course taught by the instructor
    instructors = root.find('.//instructors')
    instructor = next((i for i in instructors.findall('.//instructor') if i.attrib.get('id') == instructor_id), None)

    if instructor is None:
        print(f"Error: Instructor with ID {instructor_id} not found in the database.")
        sys.exit(1)

    # Extract instructor name
    instructor_name = instructor.find('.//name').text

    # Find courses taught by the instructor
    relationships = root.find('.//teach_course')
    instructor_courses = relationships.findall(f".//teach_course[instructor_id='{instructor_id}']")

    # Prepare the result in XML format
    result_root = ET.Element('result')
    instructor_element = ET.SubElement(result_root, 'instructor', {'id': instructor_id, 'name': instructor_name})

    for course in instructor_courses:
        course_number = course.find('.//course_number').text
        semester = course.find('.//semester').text

        course_element = ET.SubElement(instructor_element, 'course')
        course_number_element = ET.SubElement(course_element, 'course_number')
        course_number_element.text = course_number

        semester_element = ET.SubElement(course_element, 'semester')
        semester_element.text = semester

    result_tree = ET.ElementTree(result_root)
    result_tree.write(sys.stdout.buffer, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 find_instructor_courses.py <instructor_id>")
        sys.exit(1)

    # Extract instructor ID from command-line arguments
    instructor_id = sys.argv[1]

    # Call the function to find instructor courses and print the result in XML format
    find_instructor_courses(instructor_id)
