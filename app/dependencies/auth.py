from fastapi import Depends, HTTPException

# Dummy user (change role to test)
def get_current_user():
    return {
        "id": 1,
        "name": "Karthik",
        "role": "employee"   # change to "employee"
    }

# Role permissions
ROLE_PERMISSIONS = {
    "admin": ["create:asset", "delete:asset", "view:all"],
    "employee": ["view:own"]
}

# RBAC checker
def RequirePrivilege(permission: str):
    def checker(user = Depends(get_current_user)):
        role = user["role"]
        permissions = ROLE_PERMISSIONS.get(role, [])

        if permission not in permissions:
            raise HTTPException(status_code=403, detail="Not authorized")

        return user
    return checker