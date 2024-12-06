from . import app
from pydantic import BaseModel


class Video(BaseModel):
    id: int
    title: str
    speaker: str
    url: str


@app.get("/")
def homepage():
    videos = [Video(id=1, title="Hello World", speaker="John Doe", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
              Video(id=2, title="Hello World 2", speaker="John Doe", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")]
    return videos
