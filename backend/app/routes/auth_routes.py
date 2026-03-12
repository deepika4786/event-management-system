from fastapi import APIRouter, HTTPException
from app.models.user_model import User
from app.database import users_collection

router = APIRouter()

@router.post("/register")
def register(user: User):

    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    users_collection.insert_one(user.dict())

    return {"message": "User registered successfully"}


@router.post("/login")
def login(email: str, password: str):

    user = users_collection.find_one({"email": email})

    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}