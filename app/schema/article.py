from pydantic import BaseModel


class Article(BaseModel):
    id: int
    title: str
    body: str
    author_id: int
