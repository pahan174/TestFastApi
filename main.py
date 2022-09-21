from datetime import date
from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    device: str
    date_install: date
    is_active: Union[bool, None] = True


@app.get("/ping")
def read_root():
    return {"pong"}


@app.post("/dev/{item_id}")
def update_item(item_id: int, item: Item):
    return {"device": item.device,
            "item_id": item_id,
            "date_install": item.date_install,
            "Мониторить": item.is_active}
