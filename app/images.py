from dotenv import load_dotenv
from imagekitio import DefaultHttpxClient, ImageKit
import os

load_dotenv() # load .env

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    http_client=DefaultHttpxClient(trust_env=False),
)
