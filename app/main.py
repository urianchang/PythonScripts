from fastapi import FastAPI

from app.config import settings
from app.routes.base import base_routes
from app.routes.units import units_v1


DESCRIPTION = """
Example of a Python-based microservice
"""

app = FastAPI(
    title="Python Microservice API",
    description=DESCRIPTION,
    version="1.0",
    terms_of_service="http://swagger.io/terms/",
    contact={
        "name": "Domino Data Lab",
        "url": "https://tickets.dominodatalab.com/hc/en-us",
        "email": "support@dominodatalab.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_url=settings.OPENAPI_URL,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
)

app.include_router(base_routes, prefix=settings.API_BASE_STR)
app.include_router(units_v1, prefix=settings.API_V1_STR)
