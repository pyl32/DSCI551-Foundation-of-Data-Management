import sys
import json
import requests


the_url = "https://dsci551-hw1-ae8a0-default-rtdb.firebaseio.com/"

# Check if a instructor exists in the database
def instructor_exist(student_id):
    try:
        instructor_url = requests.get(f"{the_url}/instructor.json")
        instructor_data = instructor_url.json()

        if instructor_data is not None and instructor_id in instructor_data:
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

# Function to allow a instructor to take a course in a semester
def take_course(instructor_id, course_num, semester):
    if not instructor_exist(instructor_id):
        print(f"Error: Instructor '{instructor_id}' does not exist in the database.")
        return

    if not course_exist(course_num):
        print(f"Error: Course '{course_num}' does not exist in the database.")
        return

    # Add the course to the instructor's record
    try:
        # course_data = {
        #     # 'course_number': course_num,
        #     'semester': semester
        # }
        semester_data = {'semester': semester}        

        add_url = requests.put(f"{the_url}/instructor/{instructor_id}/courses/{course_num}.json", data=json.dumps(semester_data))

        if add_url.status_code == 200:
            print(f"Instructor '{instructor_id}' takes '{course_num}' in '{semester}'.")
        else:
            print(f"Failed to find instructor in the course. Status code: {add_url.status_code}")

    except requests.exceptions.RequestException as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 take_course.py <instructor_id> <course_num> <semester>")
        sys.exit(1)

    instructor_id = sys.argv[1]
    course_num = sys.argv[2]
    semester = sys.argv[3]

    take_course(instructor_id, course_num, semester)