from fastapi import FastAPI
from typing import Optional, List
from sqlmodel import SQLModel, Field


class House(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    address: str
    price: int
    image_url: str
    description: str
    beds: int
    baths: int


class Swipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    house_id: int
    user_id: int
    is_liked: bool  # True for Right Swipe, False for Left


app = FastAPI()

# MOCK DATA: In a real app, this comes from the Postgres DB
MOCK_HOUSES = [
    {
        "id": 1,
        "address": "123 Modern Lane, Austin",
        "price": 2500,
        "image_url": "https://images.unsplash.com/photo-1568605114967-8130f3a36994",
        "description": "Beautiful modern home with floor-to-ceiling windows.",
        "beds": 3,
        "baths": 2,
    },
    {
        "id": 2,
        "address": "456 Cozy Court, Denver",
        "price": 1800,
        "image_url": "https://images.unsplash.com/photo-1570129477492-45c003edd2be",
        "description": "Charming cottage with a massive backyard.",
        "beds": 2,
        "baths": 1,
    },
]


@app.get("/")
def read_root():
    return {"message": "Housr API is live"}


@app.get("/houses", response_model=List[dict])
def get_houses():
    """Returns the stack of houses for the user to swipe through."""
    return MOCK_HOUSES


@app.post("/swipe")
def record_swipe(house_id: int, is_liked: bool):
    """Records whether the user liked or disliked a house."""
    # Here you would eventually write: db.add(Swipe(house_id=house_id, is_liked=is_liked))
    print(f"User swiped {'LIKE' if is_liked else 'NOPE'} on house {house_id}")
    return {"status": "success"}
