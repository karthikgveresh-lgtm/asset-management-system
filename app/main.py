from fastapi import FastAPI
from app.routers import employees, assets, assignments
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AssetTrackr API",
    description="Asset management system backend",
    version="1.0", 
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router)
app.include_router(assets.router)
app.include_router(assignments.router)