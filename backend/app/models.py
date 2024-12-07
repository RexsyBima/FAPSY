from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NewsModel(BaseModel):  # type: ignore
    id: Optional[int]
    title: str
    url: str
    writer: str
    date: datetime
    content: str
    img_url: str
