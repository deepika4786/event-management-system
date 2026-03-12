from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth_routes
from app.routes import event_routes
from app.routes import registration_routes

app = FastAPI(
    title="Event Management System",
    version="1.0.0"
)

# CORS (for React frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include route modules
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(event_routes.router, prefix="/events", tags=["Events"])
app.include_router(registration_routes.router, tags=["Registrations"])

@app.get("/")
def root():
    return {"message": "Event Management System API Running"}