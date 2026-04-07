from fastapi import APIRouter

router = APIRouter(prefix="/api/assignments", tags=["Assignments"])

assignments_db = []

@router.post("/")
def assign_asset(data: dict):
    """
    Assign asset to employee
    """
    data["id"] = len(assignments_db) + 1
    data["status"] = "Active"
    assignments_db.append(data)
    return data

@router.get("/")
def get_assignments():
    """
    Get all assignments
    """
    return assignments_db