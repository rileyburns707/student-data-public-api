# Student Data Public API

## Intrduction
This is a simple Flask-based API that allows users to view, add, and delete student data.  

The project is meant to demonstrate API functionality and usage. I hard coded the data in the json file since I was on a limited timeline and just wanted to display API functionality, so to manually change the data you can edit the .json file or add students through a POST call on a local server.

## Deployed API
[Student Data API on Render](https://student-data-public-api.onrender.com)

The home page is simple.
To view all students go to: https://student-data-public-api.onrender.com/students

To view an individual student go to: https://student-data-public-api.onrender.com/students/1
  - 1 can be changed to any valid student id

## Features
- View all students: `GET /students`
- View a single student by ID: `GET /students/<id>`
- Add a student: `POST /students`
- Delete a student: `DELETE /students/<id>`

I used Postman to test the API, but to run the API, I created [this](https://view-student-data.onrender.com/) static site with Render. It may take a few seconds to load on the first call since I am just using the free version of Render

## Student Data Structure
Each student object contains:
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "gpa": 3.8,
  "grade": "Senior",
  "degree": "Computer Science"
}
