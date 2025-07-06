import os

import dotenv


class Settings:
    def __init__(self):
        dotenv.load_dotenv()

        self.openai_api_key = self._must_get_env("OPENAI_API_KEY")
        self.openai_base_url = self._must_get_env("OPENAI_BASE_URL")

        self.r2_endpoint = self._must_get_env("R2_ENDPOINT")
        self.r2_access_key_id = self._must_get_env("R2_ACCESS_KEY_ID")
        self.r2_secret_access_key = self._must_get_env("R2_SECRET_ACCESS_KEY")
        self.r2_bucket = self._must_get_env("R2_BUCKET")

        self.newsletter_dir = self._must_get_env("NEWSLETTER_DIR")

        self.push_deer_key = self._must_get_env("PUSH_DEER_KEY")

    def _must_get_env(self, key: str) -> str:
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Environment variable '{key}' is not set.")
        return value


settings = Settings()