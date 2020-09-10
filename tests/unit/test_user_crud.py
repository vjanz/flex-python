import pytest
from fastapi.encoders import jsonable_encoder

from app import crud
from app.schemas import UserCreate

@pytest.mark.unit
def test_create_user(user_create: UserCreate, db) -> None:
    user_dto = UserCreate(**user_create.dict())

    user = crud.user.create(db=db, obj_in=user_dto)
    assert user.email == user_create.email
    assert isinstance(user.id, int)
    assert user

@pytest.mark.unit
def test_authenticate(user_create: UserCreate, db) -> None:
    email = user_create.email
    password = user_create.password

    user_dto = UserCreate(email=email, password=password)
    user = crud.user.create(db, obj_in=user_dto)
    auth_user = crud.user.authenticate(db, email=email, password=password)
    assert auth_user
    assert auth_user.email == user.email

@pytest.mark.unit
def test_user_not_auth(db, user_create: UserCreate) -> None:
    email = user_create.email
    password = user_create.password
    user = crud.user.authenticate(db, email=email, password=password)
    assert user is None

@pytest.mark.unit
def test_check_user_status_active(db, user_create: UserCreate):
    user = crud.user.create(db, obj_in=user_create)
    is_active = crud.user.is_active(user)
    assert is_active == True

@pytest.mark.unit
def test_check_user_status_inactive(db, user_create: UserCreate):
    user_dto = UserCreate(
        **user_create.dict(exclude={"is_active"}), is_active=False
    )
    user = crud.user.create(db, obj_in=user_dto)
    is_active = crud.user.is_active(user)
    assert user
    assert is_active == False

@pytest.mark.unit
def test_is_superadmin(user_create: UserCreate, db) -> None:
    email = user_create.email
    password = user_create.password
    user_obj = UserCreate(email=email, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_obj)

    is_superadmin = crud.user.is_superuser(user)
    assert is_superadmin

@pytest.mark.unit
def test_normal_user(user_create: UserCreate, db) -> None:
    email = user_create.email
    password = user_create.password
    user_obj = UserCreate(email=email, password=password)

    user = crud.user.create(db, obj_in=user_obj)
    is_normal_user = not crud.user.is_superuser(user)
    assert is_normal_user

@pytest.mark.unit
def test_get_user_by_id(user_create: UserCreate, db) -> None:
    email = user_create.email
    password = user_create.password
    name = user_create.full_name
    user_obj = UserCreate(email=email, password=password, full_name=name)
    user = crud.user.create(db, obj_in=user_obj)

    user_from_id = crud.user.get(db, id=user.id)

    assert user_from_id
    assert user_from_id.id == user.id
    assert user_from_id.email == user.email
    assert jsonable_encoder(user) == jsonable_encoder(user_from_id)
