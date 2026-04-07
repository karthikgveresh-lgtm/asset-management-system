from fastapi import Depends
from app.dependencies.auth import RequirePrivilege

from fastapi import APIRouter

router = APIRouter(prefix="/api/assets", tags=["Assets"])

assets_db = []

@router.post("/")
def create_asset(asset: dict):
    """
    Create a new asset
    """
    asset["id"] = len(assets_db) + 1
    asset["status"] = "Available"
    assets_db.append(asset)
    return asset

@router.get("/")
def get_assets():
    """
    Get all assets
    """
    return assets_db

@router.delete("/{id}")
def delete_asset(id: int, user=Depends(RequirePrivilege("delete:asset"))):
    """
    Delete asset (Admin only)
    """
    return {"message": f"Asset {id} deleted"}