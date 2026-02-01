from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# TS의 Interface나 C#의 Class 같은 역할
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.post("/items/")
async def create_item(item: Item): # 여기서 타입 검증이 자동으로 이뤄집니다!
    return {"item_name": item.name, "message": "성공적으로 생성됨"}