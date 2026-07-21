from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.database import Base, engine, get_db
from app import crud, schemas, models
from app.security import create_access_token, verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
 
security = HTTPBearer()

app = FastAPI(
    title="DevOps Control Center",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
@app.get("/")
def home():
    return {
        "message": "DevOps Control Center API Running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/register", response_model=schemas.UserResponse)
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = crud.get_user_by_username(
        db,
        user.username
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return crud.create_user(db, user)

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = crud.authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": db_user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    username = verify_token(token)

    user = crud.get_user_by_username(
        db,
        username
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user
@app.get("/me")
def me(
    current_user: models.User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role
    }
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



 
@app.post("/projects", response_model=schemas.ProjectResponse)
def create_project(
    project: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_project(
        db=db,
        project=project,
        owner_id=current_user.id
    )
current_user: models.User = Depends(get_current_user)