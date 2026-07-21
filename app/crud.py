from sqlalchemy.orm import Session

from app import models
from app import schemas
from app.security import hash_password, verify_password
from app.models.project import Project

def create_user(db: Session, user: schemas.UserCreate):

    hashed_pwd = hash_password(user.password)

    db_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_pwd,
        role="Engineer"
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


def get_user_by_username(db: Session, username: str):

    return (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
    )
def authenticate_user(db, username, password):
    user = get_user_by_username(db, username)

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user

def create_project(db, project, owner_id):
    db_project = Project(
        name=project.name,
        description=project.description,
        github_url=project.github_url,
        owner_id=owner_id
    )

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project
from app.models.server import Server


def create_server(db: Session, server: schemas.ServerCreate, owner_id: int):
    db_server = Server(
        name=server.name,
        host=server.host,
        username=server.username,
        port=server.port,
        owner_id=owner_id
    )

    db.add(db_server)
    db.commit()
    db.refresh(db_server)

    return db_server


def get_servers(db: Session, owner_id: int):
    return (
        db.query(Server)
        .filter(Server.owner_id == owner_id)
        .all()
    )


def delete_server(db: Session, server_id: int, owner_id: int):
    server = (
        db.query(Server)
        .filter(
            Server.id == server_id,
            Server.owner_id == owner_id
        )
        .first()
    )

    if not server:
        return None

    db.delete(server)
    db.commit()

    return server
from app.models.server import Server


def get_server_by_id(
    db: Session,
    server_id: int,
    owner_id: int
):
    return (
        db.query(Server)
        .filter(
            Server.id == server_id,
            Server.owner_id == owner_id
        )
        .first()
    )