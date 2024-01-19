from fastapi import APIRouter

from app.models.check import HealthCheck


base_routes = APIRouter()


@base_routes.get("/healthcheck", response_model=HealthCheck)
def healthcheck():
    return HealthCheck(status="Healthy")
