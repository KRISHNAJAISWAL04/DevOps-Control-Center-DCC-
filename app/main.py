from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.models.server import Server
from app.database import Base, engine, get_db
from app import crud, schemas, models
from app.security import create_access_token, verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services.bootstrap import BOOTSTRAP_COMMAND
from app.services.ssh_service import execute_command, deploy_container
 
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
@app.post("/servers", response_model=schemas.ServerResponse)
def create_server(
    server: schemas.ServerCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_server(
        db=db,
        server=server,
        owner_id=current_user.id
    )


@app.get("/servers", response_model=list[schemas.ServerResponse])
def get_servers(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_servers(
        db,
        current_user.id
    )


@app.delete("/servers/{server_id}")
def delete_server(
    server_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    server = crud.delete_server(
        db,
        server_id,
        current_user.id
    )

    if server is None:
        raise HTTPException(
            status_code=404,
            detail="Server not found"
        )

    return {
        "message": "Server deleted successfully"
    }
@app.post("/servers/{server_id}/execute")
def execute_on_server(
    server_id: int,
    request: schemas.CommandRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    server = crud.get_server_by_id(
    db=db,
    server_id=server_id,
    owner_id=current_user.id
)

    if not server:
        raise HTTPException(
            status_code=404,
            detail="Server not found"
        )

    result = execute_command(
        host=server.host,
        username=server.username,
        key_path=r"C:\Users\krish\OneDrive\Desktop\agentic ai agents\intership\DevOps Control Center (DCC)\dcc-key",
        command=request.command
    )

    return result
@app.post("/servers/{server_id}/deploy")
def deploy(
    server_id: int,
    request: schemas.DeployRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    server = crud.get_server_by_id(
        db=db,
        server_id=server_id,
        owner_id=current_user.id
    )

    if not server:
        raise HTTPException(
            status_code=404,
            detail="Server not found"
        )

    command = deploy_container(
        image=request.image,
        container_name=request.container_name
    )

    result = execute_command(
        host=server.host,
        username=server.username,
        key_path=r"C:\Users\krish\OneDrive\Desktop\agentic ai agents\intership\DevOps Control Center (DCC)\dcc-key",
        command=command
    )

    return result


@app.post("/servers/{server_id}/bootstrap")
def bootstrap_server(
    server_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    server = crud.get_server_by_id(
        db=db,
        server_id=server_id,
        owner_id=current_user.id
    )

    if not server:
        raise HTTPException(
            status_code=404,
            detail="Server not found"
        )

    result = execute_command(
        host=server.host,
        username=server.username,
        key_path=server.ssh_key_path,
        command=BOOTSTRAP_COMMAND
    )

    return result
 
