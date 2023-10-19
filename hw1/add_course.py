import sys
import json
import requests

# Firebase Realtime Database URL
course_url = "https://dsci551-hw1-ae8a0-default-rtdb.firebaseio.com/course.json" 

def add_course(course_num, course_title, semester):
    course_data = {
        'course_number': course_num,
        'course_title': course_title,
        'semester': semester
    }

    try:
        response = requests.put(course_url, data=json.dumps(course_data))

        if response.status_code == 200:
            print(f"Course '{course_title}' with Course number '{course_num}' added to the database.")
        else:
            print(f"Failed to add course. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python3 add_course.py <course_number> <course_title> <semester>")
        sys.exit(1)

    course_num = sys.argv[1]
    course_title = sys.argv[2]
    semester = sys.argv[3]

    add_course(course_num, course_title, semester)
