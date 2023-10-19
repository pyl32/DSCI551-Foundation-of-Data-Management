import sys
import json
import requests


the_url = "https://dsci551-hw1-ae8a0-default-rtdb.firebaseio.com/"

# Check if a student exists in the database
def student_exist(student_id):
    try:
        student_url = requests.get(f"{the_url}/student.json")
        student_data = student_url.json()

        if student_data is not None and student_id in student_data:
            return True
        else:
            return False

    except requests.exceptions.RequestException as ex:
        print(f"Error: {ex}")
        return False

# Check if a course exists in the database
def course_exist(course_num):
    try:
        course_url = requests.get(f"{the_url}/course/course_number.json")
        course_data = course_url.json()
        print(course_url)

        if course_data is not None and course_num in course_data:
            return True
        else:
            return False

    except requests.exceptions.RequestException as ex:
        print(f"Error: {ex}")
        return False

# Function to allow a student to take a course in a semester
def take_course(student_id, course_num, semester):
    if not student_exist(student_id):
        print(f"Error: Student '{student_id}' does not exist in the database.")
        return

    if not course_exist(course_num):
        print(f"Error: Course '{course_num}' does not exist in the database.")
        return

    # Add the course to the student's record
    try:
        # course_data = {
        #     'course_number': course_num,
        #     #'semester': semester
        # }
        semester_data = {'semester': semester}

        # add_url = requests.put(f"{the_url}/student/{student_id}/courses.json", data=json.dumps(course_data))
        more_url= requests.put(f"{the_url}/student/{student_id}/courses/{course_num}.json", data=json.dumps(semester_data))

        if more_url.status_code == 200:
            print(f"Student '{student_id}' takes '{course_num}' in '{semester}'.")
        else:
            print(f"Failed to find student in the course. Status code: {more_url.status_code}")

    except requests.exceptions.RequestException as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 take_course.py <student_id> <course_num> <semester>")
        sys.exit(1)

    student_id = sys.argv[1]
    course_num = sys.argv[2]
    semester = sys.argv[3]

    take_course(student_id, course_num, semester)