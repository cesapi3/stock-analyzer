from pydantic import BaseModel

# Example Pydantic models for API responses

class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float

class User(BaseModel):
    id: int
    username: str
    email: str

class ApiResponse(BaseModel):
    success: bool
    data: dict
    message: str = None
