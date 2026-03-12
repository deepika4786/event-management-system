from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime

from app.database import registrations_collection, events_collection

router = APIRouter()

# Register for event
@router.post("/register-event")
def register_event(event_id: str, user_id: str):

    # Check if event exists
    event = events_collection.find_one({"_id": ObjectId(event_id)})

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Check duplicate registration
    existing = registrations_collection.find_one({
        "event_id": event_id,
        "user_id": user_id
    })

    if existing:
        raise HTTPException(status_code=400, detail="Already registered for this event")

    # Check capacity
    count = registrations_collection.count_documents({"event_id": event_id})

    if count >= event["max_participants"]:
        raise HTTPException(status_code=400, detail="Event is full")

    registration = {
        "event_id": event_id,
        "user_id": user_id,
        "registered_at": datetime.utcnow()
    }

    registrations_collection.insert_one(registration)

    return {"message": "Successfully registered for event"}