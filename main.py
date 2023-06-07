from typing import Literal, Optional

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class PostBody(BaseModel):
    lol: str
    booleanString: Literal["True", "False"]
    something: Optional[str]

app.post("/form")
async def handle_form(body: PostBody):
    print(body.json())
