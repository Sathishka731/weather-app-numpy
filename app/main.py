from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the application
app = FastAPI()

# 2. Define a data schema using Pydantic
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

# 3. Create a GET endpoint (Read)
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

# 4. Create a GET endpoint with path parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query_param": q}

# 5. Create a POST endpoint (Create)
@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created successfully", "data": item}
