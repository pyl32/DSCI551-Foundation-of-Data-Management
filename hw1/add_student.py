import sys
import json
import requests

# Firebase Realtime Database URL
student_url = "https://dsci551-hw1-ae8a0-default-rtdb.firebaseio.com/student/" 

def add_student(student_id, student_name, program_name):
    student_data = {
        # 'student_id': student_id,
        'student_name': student_name,
        'program_name': program_name
    }

    try:
        response = requests.put(student_url+student_id+".json", data=json.dumps(student_data))

        if response.status_code == 200:
            print(f"Student '{student_name}' with ID '{student_id}' added to the database.")
        else:
            print(f"Failed to add student. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python3 add_student.py <student_id> <student_name> <program_name>")
        sys.exit(1)

    student_id = sys.argv[1]
    student_name = sys.argv[2]
    program_name = sys.argv[3]

    add_student(student_id, student_name, program_name)
