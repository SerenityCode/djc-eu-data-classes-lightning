import requests
from typing import Dict


def create_blog_post() -> Dict:
    """
    Return the blog post created by calling the placeholder API
    
    API request parameters
    ----------------------
      - title: str
        required: true
      - body: str
        required: true
      - userId: int
        required: true
      - author: str
        required: false

    Returns
    -------
        created_post: dict
            - id: int
            - title: str
            - body: str
            - userId: int

    """  
    request_data = {"title": "My New Post",
                    "body": "Lorem Ipsum",
                    "userId": 1,}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=request_data)
    created_post = response.json()
    return created_post
