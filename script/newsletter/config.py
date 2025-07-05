import os

import dotenv


class Settings:
    def __init__(self):
        dotenv.load_dotenv()

        self.openai_api_key = self._must_get_env("OPENAI_API_KEY")
        self.openai_base_url = self._must_get_env("OPENAI_BASE_URL")

        self.newsletter_dir = self._must_get_env("NEWSLETTER_DIR")

        self.push_deer_key = self._must_get_env("PUSH_DEER_KEY")

    def _must_get_env(self, key: str) -> str:
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Environment variable '{key}' is not set.")
        return value


settings = Settings()