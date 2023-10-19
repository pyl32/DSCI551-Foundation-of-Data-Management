import sys
import json
import requests

the_url = "https://dsci551-hw1-ae8a0-default-rtdb.firebaseio.com/"

def find_courses(instructor_id):
    try:
        instructor_url = requests.get(f"{the_url}/instructor/{instructor_id}/courses.json")
        instructor_courses = instructor_url.json()

        if instructor_courses is not None:
            instructor_info_url = requests.get(f"{the_url}/instructor/{instructor_id}.json")
            instructor_info = instructor_info_url.json()
            
            instructor_name = instructor_info.get("instructor_name")
            courses = []

            for course_num, course_info in instructor_courses.items():
                course = {
                    "course_number": course_num,
                    "semester": course_info.get("semester")
                }
                courses.append(course)

            result = {
                "student_name": instructor_name,
                "courses_taken": courses
            }

            return json.dumps(result, indent=4)

        else:
            return json.dumps({"error": "Instructor not found"}, indent=4)

    except requests.exceptions.RequestException as ex:
        return json.dumps({"error": f"Error: {ex}"}, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 find_instructor_courses.py <instructor_id>")
        sys.exit(1)

    instructor_id = sys.argv[1]

    instructor_courses_record = find_courses(instructor_id)
    print(instructor_courses_record)