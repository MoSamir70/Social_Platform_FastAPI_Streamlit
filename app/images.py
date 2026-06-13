from dotenv import load_dotenv
from imagekitio import ImageKit
import httpx
import os

load_dotenv() # load .env

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    base_url=os.getenv("IMAGEKIT_URL"),
    http_client=httpx.Client(trust_env=False),
)
