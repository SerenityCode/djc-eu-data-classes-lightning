import dataclasses
from typing import Optional

import requests


@dataclasses.dataclass
class RequestData:
    title: str
    body: str
    userId: int
    author: Optional[str] = None


@dataclasses.dataclass
class ResponseData:
    id: int
    title: str
    body: str
    userId: int


def create_blog_post() -> ResponseData:
    request_data = RequestData(title="My New Post", 
                               body="Lorem Ipsum",
                               userId=1,)
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=request_data.__dict__)
    created_post = ResponseData(**response.json())
    return created_post