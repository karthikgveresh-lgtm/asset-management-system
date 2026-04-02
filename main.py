class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.assets = []

    def __str__(self):
        return f"{self.emp_id} - {self.name}"


class Asset:
    def __init__(self, asset_id, name):
        self.asset_id = asset_id
        self.name = name
        self.status = "Available"
        self.assigned_to = None

    def __str__(self):
        assigned = self.assigned_to.name if self.assigned_to else "None"
        return f"{self.asset_id} - {self.name} | {self.status} | Assigned to: {assigned}"


class AssetManagementSystem:
    def __init__(self):
        self.employees = {}
        self.assets = {}

    # Add Employee
    def add_employee(self, emp_id, name):
        if emp_id in self.employees:
            print("Employee already exists!")
            return
        self.employees[emp_id] = Employee(emp_id, name)
        print("Employee added successfully!")

    # Add Asset
    def add_asset(self, asset_id, name):
        if asset_id in self.assets:
            print("Asset already exists!")
            return
        self.assets[asset_id] = Asset(asset_id, name)
        print("Asset added successfully!")

    # Assign Asset
    def assign_asset(self, asset_id, emp_id):
        if asset_id not in self.assets:
            print("Asset not found!")
            return

        if emp_id not in self.employees:
            print("Employee not found!")
            return

        asset = self.assets[asset_id]

        if asset.status == "Assigned":
            print("Asset already assigned!")
            return

        employee = self.employees[emp_id]
        asset.status = "Assigned"
        asset.assigned_to = employee
        employee.assets.append(asset)

        print("Asset assigned successfully!")

    # Return Asset
    def return_asset(self, asset_id):
        if asset_id not in self.assets:
            print("Asset not found!")
            return

        asset = self.assets[asset_id]

        if asset.status == "Available":
            print("Asset is already available!")
            return

        employee = asset.assigned_to
        employee.assets.remove(asset)

        asset.status = "Available"
        asset.assigned_to = None

        print("Asset returned successfully!")

    # View Assets
    def view_assets(self):
        for asset in self.assets.values():
            print(asset)

    # View Employees
    def view_employees(self):
        for emp in self.employees.values():
            print(emp)
            for asset in emp.assets:
                print(f"   -> {asset.name}")


# CLI Interface
def main():
    system = AssetManagementSystem()

    while True:
        print("\n--- Asset Management System ---")
        print("1. Add Employee")
        print("2. Add Asset")
        print("3. Assign Asset")
        print("4. Return Asset")
        print("5. View Assets")
        print("6. View Employees")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            system.add_employee(emp_id, name)

        elif choice == "2":
            asset_id = input("Enter Asset ID: ")
            name = input("Enter Asset Name: ")
            system.add_asset(asset_id, name)

        elif choice == "3":
            asset_id = input("Enter Asset ID: ")
            emp_id = input("Enter Employee ID: ")
            system.assign_asset(asset_id, emp_id)

        elif choice == "4":
            asset_id = input("Enter Asset ID: ")
            system.return_asset(asset_id)

        elif choice == "5":
            system.view_assets()

        elif choice == "6":
            system.view_employees()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()