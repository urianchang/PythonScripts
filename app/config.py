from os import path

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_BASE_STR: str = "/api/units"
    API_V1_STR: str = "/v1"

    # It is not recommended to hide the API docs
    # https://fastapi.tiangolo.com/advanced/conditional-openapi/
    OPENAPI_URL: str = path.join(API_BASE_STR, "openapi.json")
    DOCS_URL: str = path.join(API_BASE_STR, "swagger")
    REDOC_URL: str = path.join(API_BASE_STR, "redoc")

    class Config:
        case_sensitive = True


settings = Settings()
