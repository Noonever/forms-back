from typing import Literal, Optional
from pydantic import BaseModel


class PostBody(BaseModel):
    pass


class FormData(BaseModel):
    url: str
    post_body: PostBody


class SomeForm(PostBody):
    pass