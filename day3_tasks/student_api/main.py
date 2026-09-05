from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Optional,Annotated


app = FastAPI()
class Address(BaseModel):
    city:str
    state : str
    pincode : int
class Course(BaseModel):
    course_name:Annotated[str,Field(min_length = 3, max_length=50)]
    course_code:Annotated[str,Field(min_length=3,max_length=10)]
    credits : Annotated[int,Field(ge=1,le=5)]

class Student_registration_model(BaseModel):
    name:Annotated[str,Field(min_length= 2, max_length=30)]
    age : Annotated[int , Field(ge=18 ,le=25)]
    dept: str
    college: str = "PEC"
    mobile_no:Optional[str] = None
    address : Address
    courses : Annotated[list[Course],Field(min_length=1,max_length=4)] # type: ignore
    # skills : Annotated[list[str] , Field(min_length= 1, max_length = 5)]



@app.post("/student")
def create_student_base(student:Student_registration_model):
    total_credit = sum(course.credits for course in student.courses )
    if student.dept != "CSBS":
        raise HTTPException(
            status_code = 400,
            detail = "Only CSBS students are allowed"
        )
    if total_credit > 12:
        raise HTTPException(
            status_code = 400,
            detail = "Maximum 12 credits  allowed"
        )
    return {
        "message":"Student created",
        "student":student.model_dump()
    }