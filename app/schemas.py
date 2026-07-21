from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str
class ProjectCreate(BaseModel):
    name: str
    description: str
    github_url: str


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    github_url: str
    owner_id: int

    class Config:
        from_attributes = True
        
class ServerCreate(BaseModel):
    name: str
    host: str
    username: str
    port: int = 22


class ServerResponse(BaseModel):
    id: int
    name: str
    host: str
    username: str
    port: int
    owner_id: int

    class Config:
        from_attributes = True

class CommandRequest(BaseModel):
    command: str