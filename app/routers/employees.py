from fastapi import APIRouter
from app.schemas import Employee

router = APIRouter(prefix="/api/employees", tags=["Employees"])

employees_db = []

@router.post("/")
def create_employee(employee: Employee):
    """
    Create a new employee

    Parameters:
    - name: string
    - email: string
    - department: string

    Returns:
    - Created employee object
    """
    emp_dict = employee.dict()
    emp_dict["id"] = len(employees_db) + 1
    employees_db.append(emp_dict)
    return emp_dict


@router.get("/")
def get_all_employees():
    """
    Get all employees

    Returns:
    - List of employees
    """
    return employees_db