import sys
import json
import requests

# Firebase Realtime Database URL
instructor_url = "https://dsci551-hw1-ae8a0-default-rtdb.firebaseio.com/instructor/" 

def add_instructor(instructor_id, instructor_name, department):
    instructor_data = {
        #'instructor_id': instructor_id,
        'instructor_name': instructor_name,
        'department': department
    }

    try:
        response = requests.put(instructor_url+instructor_id+".json", data=json.dumps(instructor_data))

        if response.status_code == 200:
            print(f"Instructor '{instructor_name}' with ID '{instructor_id}' added to the database.")
        else:
            print(f"Failed to add instructor. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python3 add_instructor.py <instructor_id> <instructor_name> <department>")
        sys.exit(1)

    instructor_id = sys.argv[1]
    instructor_name = sys.argv[2]
    department = sys.argv[3]

    add_instructor(instructor_id, instructor_name, department)