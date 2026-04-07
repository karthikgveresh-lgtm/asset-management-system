from fastapi import FastAPI
from app.routers import employees, assets, assignments

app = FastAPI(
    title="AssetTrackr API",
    description="Asset management system backend",
    version="1.0"
)

app.include_router(employees.router)
app.include_router(assets.router)
app.include_router(assignments.router)