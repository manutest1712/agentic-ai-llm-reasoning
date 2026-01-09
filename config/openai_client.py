import os
from openai import OpenAI


def get_openai_client():
    return OpenAI(
        base_url=os.getenv(
            "OPENAI_BASE_URL",
            "https://openai.vocareum.com/v1"
        ),
        api_key=os.getenv("OPENAI_API_KEY"),
    )