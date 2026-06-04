import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    base_url = os.getenv(
        "BASE_URL",
        "https://restful-booker.herokuapp.com",
    )

    username = os.getenv("BOOKER_USERNAME", "admin")
    password = os.getenv("BOOKER_PASSWORD", "password123")


settings = Settings()