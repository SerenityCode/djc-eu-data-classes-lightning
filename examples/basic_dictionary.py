from typing import Dict
import requests


def create_blog_post() -> Dict:
    request_data = {"title": "My New Post",
                    "body": "Lorem Ipsum",
                    "userId": 1,}

    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=request_data)
    created_post = response.json()
    return created_post
