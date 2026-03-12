from fastapi import APIRouter
from bson import ObjectId

from app.models.event_model import Event
from app.database import events_collection

router = APIRouter()

# Create event
@router.post("/")
def create_event(event: Event):

    event_data = event.dict()

    events_collection.insert_one(event_data)

    return {"message": "Event created successfully"}


# List all events
@router.get("/")
def get_events():

    events = list(events_collection.find())

    for event in events:
        event["_id"] = str(event["_id"])

    return {"events": events}


# Update event
@router.put("/{event_id}")
def update_event(event_id: str, event: Event):

    events_collection.update_one(
        {"_id": ObjectId(event_id)},
        {"$set": event.dict()}
    )

    return {"message": "Event updated successfully"}


# Delete event
@router.delete("/{event_id}")
def delete_event(event_id: str):

    events_collection.delete_one({"_id": ObjectId(event_id)})

    return {"message": "Event deleted successfully"}