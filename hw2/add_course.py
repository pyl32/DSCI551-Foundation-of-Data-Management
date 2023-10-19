import sys
from lxml import etree as ET

xml_path = 'hw2.xml'

def add_course(course_number, course_title, semester):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except ET.XMLSyntaxError as e:
        print(f"Error parsing XML file: {e}")
        sys.exit(1)

    new_course = ET.Element('course', {'number': course_number})

    title_element = ET.Element('title')
    title_element.text = course_title
    new_course.append(title_element)

    semester_element = ET.Element('semester')
    semester_element.text = semester
    new_course.append(semester_element)

    root.find('.//courses').append(new_course)  # Using XPath for finding courses

    tree.write(xml_path, pretty_print=True, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 add_course.py <course_number> <course_title> <semester>")
        sys.exit(1)

    course_number, course_title, semester = sys.argv[1], sys.argv[2], sys.argv[3]

    add_course(course_number, course_title, semester)

    print(f"Course {course_number} added successfully.")

