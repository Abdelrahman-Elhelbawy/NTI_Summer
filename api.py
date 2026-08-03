from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True        # default -> optional

@app.post("/items")
def create_item(item: Item):     # JSON body -> validated Item
    return {"name": item.name, "total": item.price * 1.2}