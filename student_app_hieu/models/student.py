from pydantic import BaseModel, field_validator
from typing import Optional

class StudentCreate(BaseModel):
    id: str 
    name: str
    age: int
    gpa: float 
    # thêm đk tên không được để trống hay là các khoảng trắng
    @field_validator('id', 'name')
    def not_empty(cls, v, info):
        if v is None or (isinstance(v, str) and not v.strip()):
            raise ValueError(f"{info.field_name} khong duoc de trong")
        return v
    
    @field_validator('age')
    def age_valid(cls, v, info):
        if not (1 <= v <= 60):
            raise ValueError("Tuoi khong hop le")
        return v
    #gpa phải hợp lệ
    @field_validator('gpa')
    def gpa_valid(cls, v, info):
        if not (0.0 <= v <= 10.0):
            raise ValueError("GPA khong hop le")
        return v
    

class StudentUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    age: Optional[int] = None 
    gpa: Optional[float] = None 

    @field_validator('id', 'name')
    def not_empty(cls, v, info):
        if v is None or (isinstance(v, str) and not v.strip()):
            raise ValueError(f"{info.field_name} khong duoc de trong")
        return v
    
    @field_validator('age')
    def age_valid(cls, v, info):
        if not (1 <= v <= 60):
            raise ValueError("Tuoi khong hop le")
        return v

    @field_validator('gpa')
    def gpa_valid(cls, v, info):
        if not (0.0 <= v <= 10.0):
            raise ValueError("GPA khong hop le")
        return v
    
class StudentOut(BaseModel):


    # cho phép chuyển đổi từ ORM model sang Pydantic model
    @classmethod
    def from_orm(cls, orm_model):
        return cls(
            id=orm_model.id,
            name=orm_model.name,
            age=orm_model.age,
            gpa=orm_model.gpa
        )

