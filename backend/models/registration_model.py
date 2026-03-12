from pydantic import BaseModel

class Registration(BaseModel):
    event_id: str
    user_id: str