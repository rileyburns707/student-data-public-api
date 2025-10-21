"""
main.py
-------
This is a basic flask application. The application stores students from the 
students.json file. It is hard coded becuase this project is about API functionality
not data management.
"""
from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__) 
CORS(app)  # allows requests from any origin

with open("students.json") as data_file:
    students = json.load(data_file) 

@app.route('/')
def home_page():
    """
    This is the main page of the application
    """
    return "Student data public API home page"

@app.route("/students", methods=["GET"])
def get_students():
    """
    This is function returns all students.
    """
    return students

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    """
    This is function returns individual students based off their id.
    Changing the id in the url will change the data being retrieved. 

    Since I am calling from a json file I have to loop through each student,
    but if this was requesting from a database then I could run ".query.get_or_404(id)"
    to make it easier.
    """
    student = next((student for student in students if student["id"] == id), None)
    if student:
        return student
    return {"Error": "Student not found"}, 404

@app.route('/students', methods=['POST'])
def add_student():
  """
  This function adds a student to the json file
  """
  student_data = request.get_json()
  required_student_data = ["id", "name", "gpa", "grade", "degree"]
  if not all(field in student_data for field in required_student_data):
     return {"error": "Missing fields"}, 400
  
  students.append(student_data)

  # Write back to JSON file
  with open("students.json", "w") as data_file:
      json.dump(students, data_file, indent=4)

  return {"message": "Student successfuly added", "student": student_data}, 201

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    """
    This function deletes a student from the json file
    """
    global students
    student = next((student for student in students if student["id"] == id), None)
    if student:
      students = [student for student in students if student["id"] != id]

      # Write back to JSON file
      with open("students.json", "w") as data_file:
          json.dump(students, data_file, indent=4)

      return {"message": f"Student successfuly deleted"}, 201
    
    return {"error": "Student not found"}, 404