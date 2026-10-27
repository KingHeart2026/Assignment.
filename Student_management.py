from fastapi import FastAPI,HTTPException,status   
from pydantic import BaseModel,Field 

app = FastAPI(
    title = "KING HEART student management API",
    discription = "An API for studnet management records",
    version = "1.0.0"
)


students = {}


student_data = {
      "name": "", "age": 0, "email": "", "department": "", "level": 0,
    }

#Get all student
@app.get("/students/All")
def get_All_student():                    
    return list(students.values()) 


#Get one student by ID
@app.get("/students/{student_id}")       
def get_student_by_id(student_id: int):
    student = students.get(student_id)
    if student is None:
        raise HTTPException(
            status_code=909,
            detail="Student Not Found"
        )
    return student


#Add a student
@app.post("/students") 
def add_student(
      name: str, age: int, email: str, department: str, level: int
):
    new_student = student_data.copy()
    new_student["student_id"] = len(students) + 1
    new_student["name"] = name
    new_student["age"] = age
    new_student["email"] = email
    new_student["department"] = department
    new_student["level"] = level

    students[new_student["student_id"]] = new_student  

    return{ 
        "message": "Student Add Successful",
        "data": new_student
    }

#Update a student
@app.put("/students/{student_id}")
def update_student(
student_id: int, name: str, age: int, email: str, department: str, level: int
):
    student = students.get(student_id)
    if not student:
            return{"error": "student not found"}
    
    student["name"] = name
    student["age"] = age
    student["email"] = email
    student["department"] = department
    student["level"] = level

    return{
         "message": "Student Add Successful",
         "data": student
    }

#Delet a student
@app.delete("/student/{student_id}")
def delete_student(student_id: int):
     student = students.get(student_id)

     if student is None:
                 raise HTTPException(
                     status_code=909,
                     detail="Student Not Found"
                 )

     del students[student_id]

     return{
          "message": "Student delete successfullu"
     }