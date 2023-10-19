import sys
import json
import requests


the_url = "https://dsci551-hw1-ae8a0-default-rtdb.firebaseio.com/"

def find_courses(student_id):
    try:
        student_url = requests.get(f"{the_url}/student/{student_id}/courses.json")
        student_courses = student_url.json()

        if student_courses is not None:
            student_info_url = requests.get(f"{the_url}/student/{student_id}.json")
            student_info = student_info_url.json()
            
            student_name = student_info.get("student_name")
            courses = []

            for course_num, course_info in student_courses.items():
                course = {
                    "course_number": course_num,
                    "semester": course_info.get("semester")
                }
                courses.append(course)

            result = {
                "student_name": student_name,
                "courses_taken": courses
            }

            return json.dumps(result, indent=4)

        else:
            return json.dumps({"error": "Student not found"}, indent=4)

    except requests.exceptions.RequestException as ex:
        return json.dumps({"error": f"Error: {ex}"}, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 find_student_courses.py <student_id>")
        sys.exit(1)

    student_id = sys.argv[1]

    student_courses_record = find_courses(student_id)
    print(student_courses_record)